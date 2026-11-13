"""The generated layer against spec/: everything is derived from the spec files, so a regeneration
does not need to touch this test."""

from __future__ import annotations

import hashlib
import hmac
import importlib.util
import json
import re
import time
import typing
from pathlib import Path
from typing import Any, Dict, Literal, Optional

from funnelchat import ROUTE_GROUPS, ROUTES, WEBHOOK_EVENTS, types
from funnelchat.resources import Devices
from funnelchat.webhooks import construct_event

ROOT = Path(__file__).resolve().parent.parent
SPEC = json.loads((ROOT / "spec" / "funnelchat.json").read_text("utf-8"))
PENDING = json.loads((ROOT / "spec" / "pending.json").read_text("utf-8"))
MANIFEST = json.loads((ROOT / "spec" / "resources.json").read_text("utf-8"))
METHODS = ("get", "put", "post", "delete", "patch")

_loader = importlib.util.spec_from_file_location("generate", ROOT / "scripts" / "generate.py")
assert _loader and _loader.loader
generate: Any = importlib.util.module_from_spec(_loader)
_loader.loader.exec_module(generate)


def spec_op(method: str, path: str) -> Dict[str, Any]:
    return SPEC["paths"].get(path, {}).get(method.lower())


def test_generated_files_and_readme_block_are_up_to_date() -> None:
    assert generate.main(["--check"]) == 0


def test_types_exactly_what_the_spec_publishes() -> None:
    assert "paths" not in PENDING
    published = sorted((m.upper(), p) for p, item in SPEC["paths"].items() for m in METHODS if m in item)
    assert sorted((r.method, r.path) for r in ROUTES) == published
    events = [e.type for e in WEBHOOK_EVENTS]
    assert len(set(events)) == len(events)
    assert set(events) == {re.sub(r"\s*\(.*\)\s*$", "", key) for key in SPEC["webhooks"]}
    # Every method of a resource is an operation the spec publishes.
    assert [m["op"] for r in MANIFEST["resources"] for m in r["methods"] if not spec_op(*m["op"].split(" ", 1))] == []


def test_each_route_has_its_group_category_and_whether_it_can_be_undone() -> None:
    for r in ROUTES:
        op = spec_op(r.method, r.path)
        destructive = op.get("x-fc-destructive")
        assert r.destructive == (destructive if isinstance(destructive, bool) else None)
        assert r.tag == (op.get("tags") or [None])[0]
        assert r.category == next((g.category for g in ROUTE_GROUPS if g.name == r.tag), None)
    assert sum(g.operations for g in ROUTE_GROUPS) == sum(1 for r in ROUTES if r.tag)
    # The portal names a category by its id in x-tagGroups; the routes carry the title it shows.
    titles = {c["id"]: c["title"] for c in SPEC.get("x-fc-categorias", [])}
    for entry in (e for e in SPEC.get("x-tagGroups", []) if e.get("x-fc-categoria") in titles):
        assert {g.category for g in ROUTE_GROUPS if g.name in entry["tags"]} == {titles[entry["x-fc-categoria"]]}
    # A method of an operation that cannot be undone says so to whoever reads it, a person or an agent.
    assert "cannot be undone" in (Devices.delete.__doc__ or "")


def test_group_events_carry_the_message_uid_production_sends() -> None:
    for name in ("GroupMessageReceivedEventDataMessage", "GroupReactionAddedEventDataMessage"):
        fields = getattr(types, name).__annotations__
        assert "uid" in fields and "id" not in fields, name


def test_every_type_resolves_at_runtime() -> None:
    # pydantic and FastAPI read a TypedDict with typing.get_type_hints, on every Python the SDK supports.
    classes = [value for value in vars(types).values() if isinstance(value, type) and issubclass(value, dict) and value is not dict]
    assert len(classes) > 300
    for cls in classes:
        typing.get_type_hints(cls)


def test_names_of_a_published_release_still_import() -> None:
    for name in generate.RETIRED_TYPES:
        assert name in types.__all__ and hasattr(types, name), name


def test_events_type_what_production_sends() -> None:
    for name in ("GroupJoinRequestCreatedEventDataParticipant", "GroupJoinRequestRevokedEventDataParticipant"):
        participant = typing.get_type_hints(getattr(types, name))
        assert participant["identity"] is str and participant["name"] == Optional[str], name
        assert participant["identity_type"] == Literal["phone", "whatsapp_user"], name
    answer = typing.get_type_hints(types.WhatsappFormCompletedEventDataAnswersItem)
    assert answer["label"] is str and type(None) in typing.get_args(answer["value"])
    # A type of message the spec does not list yet is a string too, and the event is read as it comes.
    known, other = typing.get_args(typing.get_type_hints(types.MessageReceivedEventDataMessage)["type"])
    assert "text" in typing.get_args(known) and other is str
    body = json.dumps({"id": "evt_1", "type": "message.received", "version": 1, "occurred_at": "2026-11-13T12:00:00Z", "data": {"message": {"id": 1, "type": "a_new_kind", "text": None, "media": None}}})
    t = int(time.time())
    header = f"t={t},v1={hmac.new(b'whsec_test', f'{t}.{body}'.encode(), hashlib.sha256).hexdigest()}"
    assert construct_event(body, header, "whsec_test")["data"]["message"]["type"] == "a_new_kind"


def test_portal_groups_read_the_category_as_the_spec_gives_it() -> None:
    tags = [{"name": "Números"}, {"name": "Mensajes"}, {"name": "Ventas"}]

    def categories(spec: Dict[str, Any]) -> Any:
        groups, warnings, _ = generate.portal_groups(spec)
        return {name: g["category"] for name, g in groups.items()}, warnings

    each_its_own = {"tags": tags, "x-tagGroups": [{"name": t["name"], "tags": [t["name"]]} for t in tags]}
    assert categories(each_its_own) == ({"Números": None, "Mensajes": None, "Ventas": None}, [])

    expected = {"Números": "Funciones de WhatsApp", "Mensajes": "Funciones de WhatsApp", "Ventas": "Funciones de Funnelchat"}
    own_key = {
        "tags": tags,
        "x-tagGroups": [
            {"name": "Números", "tags": ["Números"], "x-fc-categoria": "Funciones de WhatsApp"},
            {"name": "Mensajes", "tags": ["Mensajes"], "x-fc-categoria": {"nombre": "Funciones de WhatsApp"}},
            {"name": "Ventas", "tags": ["Ventas"], "x-fc-categoria": "funnelchat"},
        ],
        "x-fc-categorias": [{"id": "funnelchat", "title": "Funciones de Funnelchat", "url": "https://example.com/funnelchat/"}],
    }
    grouped = {
        "tags": tags,
        "x-tagGroups": [
            {"name": "Funciones de WhatsApp", "tags": ["Números", "Mensajes"]},
            {"name": "Funciones de Funnelchat", "tags": ["Ventas"]},
        ],
    }
    assert categories(own_key) == (expected, [])
    assert categories(grouped) == (expected, [])

    unreadable = {"tags": tags, "x-tagGroups": [{"name": "Números", "tags": ["Números"], "x-fc-categoria": ["a", "b"]}]}
    found, warnings = categories(unreadable)
    assert found["Números"] is None and len(warnings) == 1


def test_readme_block_lists_the_groups_by_category() -> None:
    def group(name: str, category: Any) -> Dict[str, Any]:
        return {"name": name, "category": category}

    assert "\n- Números, Ventas." in generate.readme_block([group("Números", None), group("Ventas", None)], 2, 1)
    catalog = [{"name": "Funciones de Funnelchat", "url": "https://example.com/funnelchat/"}, {"name": "Funciones de WhatsApp", "url": None}]
    block = generate.readme_block(
        [group("Números", "Funciones de WhatsApp"), group("Notas", None), group("Ventas", "Funciones de Funnelchat")], 3, 1, catalog
    )
    # In the order of the spec's list of categories, each one with its page; a group without one goes last.
    assert block.endswith(
        "\n- **[Funciones de Funnelchat](https://example.com/funnelchat/):** Ventas."
        "\n- **Funciones de WhatsApp:** Números."
        "\n- **Without a category:** Notas."
    )
