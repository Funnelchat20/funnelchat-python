#!/usr/bin/env python3
"""The single generation script of the SDK. Standard library only, Python 3.9 or later.

    python scripts/generate.py                    regenerate from spec/funnelchat.json
    python scripts/generate.py --spec <file>      copy a new full unified spec of the portal into
                                                  spec/, record where it came from in
                                                  spec/procedencia.json, then regenerate
    python scripts/generate.py --pending <file>   copy spec/pending.json from a checkout of
                                                  funnelchat-node, record where it came from in
                                                  spec/procedencia.json, then regenerate
    python scripts/generate.py --check            regenerate in memory and fail if a generated file
                                                  differs

With --spec, when the file is not inside a checkout of the repository it was built from (a copy, or
a build output git ignores), say where it came from: `--source key=value` (repository, path, branch,
commit, commit_date, file_tracked_in_git), recorded as declared, not read from git;
`--domain <domain>=<sha>@<branch>@<snapshot_at>` for the snapshot of an area the spec does not date
itself; and `--expect-sha256 <hex>` to refuse a file that is not the one announced. The same flags,
the same file and the same merge rules as `npm run generate` in funnelchat-node.

Steps:
  1. (with --spec / --pending) copy the file and record its provenance.
  2. Merge spec/pending.json (the "pending of the spec" layer, kept in funnelchat-node and copied
     here as is) into the spec: every entry applies only while the spec lacks it, and the report
     lists the entries a new spec made obsolete.
  3. src/funnelchat/_routes.py   every operation (method, path, area, permission) and the event
                                 catalog. The SDK reads the permission to know which requests are
                                 sends, which are never retried automatically.
  4. src/funnelchat/types.py     TypedDicts: the schemas the methods of the SDK use, the response of
                                 each method and every webhook event (from its schema when it lists
                                 its properties and which are required, otherwise from its example).
  5. src/funnelchat/resources.py the resources of spec/resources.json: each method's path
                                 parameters, keyword arguments (query or body) and return type come
                                 from its operation.

Nothing in the generated files is edited by hand, and they name a permission only as the panel does
(**WhatsApp numbers → View**), never by its literal, except in the `permission` of the route table:
the generation fails if they do.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import keyword
import re
import subprocess
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
SPEC_FILE = ROOT / "spec" / "funnelchat.json"
PROVENANCE_FILE = ROOT / "spec" / "procedencia.json"
PENDING_FILE = ROOT / "spec" / "pending.json"
RESOURCES_FILE = ROOT / "spec" / "resources.json"
PACKAGE = ROOT / "src" / "funnelchat"
HTTP_METHODS = ["get", "put", "post", "delete", "patch"]

# Keyword arguments every method may take besides the ones of the operation: no field of a body or a
# query can be called like these (the generation fails if one is).
REQUEST_OPTIONS = (
    "extra_query",
    "extra_body",
    "extra_headers",
    "timeout",
    "max_retries",
    "retry_send",
    "idempotency_key",
)


class GenerationError(Exception):
    pass


# ---- Arguments ---------------------------------------------------------------------------------

DECLARABLE_SOURCE_KEYS = ("repository", "path", "branch", "commit", "commit_date", "file_tracked_in_git")


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Regenerate the SDK from spec/.")
    parser.add_argument("--spec", help="a new full unified spec of the portal to copy into spec/")
    parser.add_argument("--source", action="append", default=[], help="key=value: where the spec came from")
    parser.add_argument("--domain", action="append", default=[], help="<domain>=<sha>@<branch>@<snapshot_at>")
    parser.add_argument("--expect-sha256", dest="expect_sha256", help="refuse a spec with another sha256")
    parser.add_argument("--pending", help="a spec/pending.json of funnelchat-node to copy into spec/")
    parser.add_argument("--check", action="store_true", help="fail if a generated file is out of date")
    args = parser.parse_args(argv)
    if args.check and (args.spec or args.pending):
        raise GenerationError("--check cannot be combined with --spec or --pending")
    if (args.source or args.domain or args.expect_sha256) and not args.spec:
        raise GenerationError("--source, --domain and --expect-sha256 go with --spec")
    args.declared = {}
    for pair in args.source:
        key, sep, value = pair.partition("=")
        if not sep or key not in DECLARABLE_SOURCE_KEYS:
            raise GenerationError(f"--source takes key=value, with key one of: {', '.join(DECLARABLE_SOURCE_KEYS)}")
        args.declared[key] = (value == "true") if key == "file_tracked_in_git" else value
    args.domains = {}
    for pair in args.domain:
        match = re.fullmatch(r"([a-z-]+)=([0-9a-f]{7,40})@([^@]+)@([^@]+)", pair)
        if not match:
            raise GenerationError("--domain takes <domain>=<sha>@<branch>@<snapshot_at>")
        domain, sha, branch, snapshot_at = match.groups()
        args.domains[domain] = {"sha": sha, "branch": branch, "snapshot_at": snapshot_at}
    return args


# ---- Step 1: provenance ------------------------------------------------------------------------


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(cwd: Path, *args: str) -> Optional[str]:
    try:
        out = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.strip()


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def mtime_iso(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def git_source(path: Path) -> Tuple[Optional[Path], Dict[str, Any]]:
    """What git says about a file: its checkout, branch, commit and whether it is tracked and clean."""
    top_text = git(path.parent, "rev-parse", "--show-toplevel")
    top = Path(top_text) if top_text else None
    rel = str(path.resolve().relative_to(top.resolve())) if top else None
    tracked = (git(top, "ls-files", "--error-unmatch", rel) is not None) if top else None
    dirty = git(top, "status", "--porcelain", "--untracked-files=no") if top else None
    return top, {
        "repository": git(top, "remote", "get-url", "origin") if top else None,
        "path": rel,
        "branch": git(top, "branch", "--show-current") if top else None,
        "commit": git(top, "rev-parse", "HEAD") if top else None,
        "commit_date": git(top, "log", "-1", "--format=%cI") if top else None,
        "file_tracked_in_git": tracked,
        "tracked_files_clean": None if dirty is None else dirty == "",
        "file_modified_at": mtime_iso(path),
    }


def read_provenance() -> Dict[str, Any]:
    if PROVENANCE_FILE.exists():
        return json.loads(PROVENANCE_FILE.read_text("utf-8"))
    return {}


def write_provenance(provenance: Dict[str, Any]) -> None:
    PROVENANCE_FILE.write_text(json.dumps(provenance, indent=2, ensure_ascii=False) + "\n", "utf-8")


def count_operations(spec: Dict[str, Any]) -> int:
    return sum(1 for item in spec.get("paths", {}).values() for m in HTTP_METHODS if m in item)


def import_spec(source: str, declared: Dict[str, Any], declared_domains: Dict[str, Any], expect: Optional[str]) -> None:
    """Copies a new spec into spec/ and records where it came from (the same fields as funnelchat-node)."""
    path = Path(source).resolve()
    data = path.read_bytes()
    if expect and sha256(data) != expect.lower():
        raise GenerationError(f"{source}: its sha256 is {sha256(data)}, not the expected {expect}.")
    spec = json.loads(data.decode("utf-8"))
    top, src = git_source(path)
    domains = []
    for s in spec.get("x-fc-sources", []):
        given = None if s.get("sha") else declared_domains.get(s.get("domain"))
        entry = {
            "domain": s.get("domain"),
            "sha": s.get("sha") or (given or {}).get("sha"),
            "branch": s.get("branch") or (given or {}).get("branch"),
            "snapshot_at": s.get("snapshot_at") or (given or {}).get("snapshot_at"),
        }
        if given:
            entry["declared"] = True
        domains.append(entry)
    if declared:
        src.update(declared)
        if top is None:
            src["tracked_files_clean"] = None
        src["declared"] = list(declared)
        src["declared_note"] = (
            "The fields in `declared` were given on the command line (`--source`), not read from git: "
            "the file was imported from outside a checkout of its repository."
        )
    previous = read_provenance()
    provenance = {
        "description": (
            "Where spec/funnelchat.json and spec/pending.json came from. Written by "
            "`python scripts/generate.py --spec <file>` and `--pending <file>`; do not edit it by hand."
        ),
        "file": "spec/funnelchat.json",
        "sha256": sha256(data),
        "bytes": len(data),
        "source": src,
        "imported_at": now_iso(),
        "spec": {
            "openapi": spec.get("openapi"),
            "title": spec.get("info", {}).get("title"),
            "version": spec.get("info", {}).get("version"),
            "paths": len(spec.get("paths", {})),
            "operations": count_operations(spec),
            "webhooks": len(spec.get("webhooks", {})),
            "domains": domains,
        },
    }
    if "pending" in previous:
        provenance["pending"] = previous["pending"]
    SPEC_FILE.parent.mkdir(parents=True, exist_ok=True)
    SPEC_FILE.write_bytes(data)
    write_provenance(provenance)
    print(f"spec: copied from {src.get('path') or path} ({src.get('branch') or '?'} @ {(src.get('commit') or '?')[:8]})")


def import_pending(source: str) -> None:
    """Copies spec/pending.json from a checkout of funnelchat-node, where that layer is kept."""
    path = Path(source).resolve()
    data = path.read_bytes()
    json.loads(data.decode("utf-8"))
    top, src = git_source(path)
    if top is not None and src["path"]:
        src["file_commit"] = git(top, "log", "-1", "--format=%H", "--", src["path"])
        src["file_clean"] = git(top, "status", "--porcelain", "--", src["path"]) == ""
    provenance = read_provenance()
    provenance["pending"] = {
        "file": "spec/pending.json",
        "sha256": sha256(data),
        "bytes": len(data),
        "note": (
            "The pending layer is kept in funnelchat-node (spec/pending.json) and copied here unchanged, "
            "so both SDKs apply the same corrections. `file_commit` is the last commit that changed it."
        ),
        "source": src,
        "imported_at": now_iso(),
    }
    PENDING_FILE.write_bytes(data)
    write_provenance(provenance)
    print(f"pending: copied from {src.get('repository') or path} ({src.get('branch') or '?'} @ {(src.get('commit') or '?')[:7]})")


# ---- Step 2: the pending layer (the same rules as funnelchat-node's scripts/generate.mjs) --------


def pointer(target: Any, key: str) -> Any:
    if not key.startswith("/"):
        return target.get(key) if isinstance(target, dict) else None
    node = target
    for part in key[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(node, dict):
            node = node.get(part)
        elif isinstance(node, list) and part.isdigit() and int(part) < len(node):
            node = node[int(part)]
        else:
            return None
    return node


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=False, ensure_ascii=False, separators=(",", ":"))


def matches(target: Any, condition: Optional[Dict[str, Any]]) -> bool:
    """Whether `target` matches every entry of `condition` (a key starting with `/` is a JSON Pointer)."""
    if not condition:
        return True
    return all(canonical(pointer(target, key)) == canonical(value) for key, value in condition.items())


def event_type_of_key(key: str) -> str:
    """The event type a `webhooks` key stands for: "webhook.test (conversations)" -> "webhook.test"."""
    return re.sub(r"\s*\(.*\)\s*$", "", key)


def merge_pending(spec: Dict[str, Any], pending: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, List[str]]]:
    merged = copy.deepcopy(spec)
    merged.setdefault("components", {}).setdefault("schemas", {})
    merged.setdefault("paths", {})
    merged.setdefault("webhooks", {})
    schemas = merged["components"]["schemas"]
    report: Dict[str, List[str]] = {"applied": [], "superseded": [], "missing": []}

    for name, schema in pending.get("components", {}).get("schemas", {}).items():
        if name in schemas:
            raise GenerationError(f"spec/pending.json: the schema {name} already exists in the spec; rename it.")
        schemas[name] = schema

    for path, item in pending.get("paths", {}).items():
        for method in HTTP_METHODS:
            if method not in item:
                continue
            label = f"{method.upper()} {path}"
            if method in merged["paths"].get(path, {}):
                report["superseded"].append(label)
                continue
            merged["paths"].setdefault(path, {})[method] = item[method]
            report["applied"].append(label)

    for patch in pending.get("operationPatches", []):
        names = list(patch.get("requestBodyProperties", {})) + [p["name"] for p in patch.get("parameters", [])]
        label = f"{patch['method'].upper()} {patch['path']} (patch: {', '.join(names)})"
        op = merged["paths"].get(patch["path"], {}).get(patch["method"])
        if not op:
            report["missing"].append(label)
            continue
        if not matches(op, patch.get("while")):
            report["superseded"].append(label)
            continue
        schema = op.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
        if schema and "$ref" in schema:
            schema = schemas.get(schema["$ref"].split("/")[-1])
        if patch.get("requestBodyProperties") and not schema:
            report["missing"].append(label)
            continue
        props = (schema or {}).get("properties", {})
        missing_props = [p for p in patch.get("requestBodyProperties", {}) if p not in props]
        present = {(p.get("name"), p.get("in")) for p in op.get("parameters", [])}
        missing_params = [p for p in patch.get("parameters", []) if (p["name"], p["in"]) not in present]
        if not patch.get("while") and not missing_props and not missing_params:
            report["superseded"].append(label)
            continue
        if schema is not None:
            schema.setdefault("properties", {})
            for prop, prop_schema in patch.get("requestBodyProperties", {}).items():
                schema["properties"].setdefault(prop, prop_schema)
        if missing_params:
            op["parameters"] = op.get("parameters", []) + missing_params
        op["x-fc-pending"] = patch.get("x-fc-pending")
        report["applied"].append(label)

    for patch in pending.get("schemaPatches", []):
        label = f"schema {patch['schema']} (patch: {', '.join(patch.get('properties', {}))})"
        schema = schemas.get(patch["schema"])
        if schema is None:
            report["missing"].append(label)
            continue
        schema.setdefault("properties", {})
        missing = [p for p in patch.get("properties", {}) if p not in schema["properties"]]
        if not missing:
            report["superseded"].append(label)
            continue
        for prop in missing:
            schema["properties"][prop] = patch["properties"][prop]
        required = [p for p in patch.get("required", []) if p in missing]
        if required:
            schema["required"] = list(dict.fromkeys(schema.get("required", []) + required))
        schema.setdefault("x-fc-pending", patch.get("x-fc-pending"))
        report["applied"].append(label)

    for patch in pending.get("responsePatches", []):
        label = f"{patch['method'].upper()} {patch['path']} (response: {', '.join(patch.get('responses', {}))})"
        op = merged["paths"].get(patch["path"], {}).get(patch["method"])
        if not op:
            report["missing"].append(label)
            continue
        if not matches(op, patch.get("while")):
            report["superseded"].append(label)
            continue
        responses = op.setdefault("responses", {})
        for code in [c for c in responses if str(c).startswith("2")]:
            del responses[code]
        responses.update(patch.get("responses", {}))
        op.setdefault("x-fc-pending", patch.get("x-fc-pending"))
        op["x-fc-pending-response"] = patch.get("x-fc-pending")
        report["applied"].append(label)

    snapshot_types = {event_type_of_key(key): key for key in merged["webhooks"]}
    for event_type, item in pending.get("webhooks", {}).items():
        label = f"webhook {event_type}"
        current = snapshot_types.get(event_type)
        if current:
            replace_while = item.get("post", {}).get("x-fc-replace-while")
            if not replace_while or not matches(merged["webhooks"][current].get("post", {}), replace_while):
                report["superseded"].append(label)
                continue
            del merged["webhooks"][current]
        merged["webhooks"][event_type] = item
        report["applied"].append(label)

    return merged, report


# ---- Permissions: the names of the panel ---------------------------------------------------------

# Each permission as the panel names it (the same table as funnelchat-node's scripts/generate.mjs).
PERMISSION_NAMES = {
    "conversations:read": "Contacts and conversations → View",
    "conversations:write": "Contacts and conversations → Edit",
    "conversations:send": "Contacts and conversations → Send",
    "communities:read": "Groups and campaigns → View",
    "communities:write": "Groups and campaigns → Edit",
    "communities:send": "Groups and campaigns → Send",
    "communities:operate": "Groups and campaigns → Manage groups",
    "accounts:read": "WhatsApp numbers → View",
    "accounts:write": "WhatsApp numbers → Edit",
    "accounts:operate": "WhatsApp numbers → Create, connect and delete",
    "webhooks:read": "Notifications (webhooks) → View",
    "webhooks:write": "Notifications (webhooks) → Manage",
}
PERMISSION_LITERAL = re.compile(r"\b(?:accounts|communities|conversations|webhooks):(?:[a-z]+\b|\*)")
ROUTE_PERMISSION_FIELD = re.compile(r'^(\s*Route\((?:"[^"]*"|None), (?:"[^"]*"|None), (?:"[^"]*"|None), (?:"[^"]*"|None), )(?:"[^"]*"|None)')


def assert_permission_names(files: Dict[str, str]) -> None:
    found = []
    for name, content in files.items():
        for number, line in enumerate(content.split("\n"), 1):
            prose = ROUTE_PERMISSION_FIELD.sub(r"\1", line) if name == "_routes.py" else line
            for literal in PERMISSION_LITERAL.findall(prose):
                found.append(f"src/funnelchat/{name}:{number}: {literal}")
    if found:
        raise GenerationError(
            "the generated files would name permissions by their literal, not as the panel does "
            "(PERMISSION_NAMES in scripts/generate.py):\n" + "\n".join(f"  - {f}" for f in found)
        )


# ---- Names ---------------------------------------------------------------------------------------


def pascal(text: str) -> str:
    words = re.findall(r"[A-Z]+(?=[A-Z][a-z]|\d|\b|_|$)|[A-Z]?[a-z]+|[A-Z]+|\d+", text)
    return "".join(w[:1].upper() + w[1:] for w in words) or "X"


def snake(text: str) -> str:
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").lower()


def is_identifier(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


def python_name(key: str) -> Optional[str]:
    """The keyword argument of a field of the API (`from` -> `from_`), or None when it cannot be one."""
    if keyword.iskeyword(key) and key.isidentifier():
        return f"{key}_"
    return key if is_identifier(key) and not key.startswith("_") else None


def split_items(text: str) -> List[str]:
    """The `"key": value` items of a dict literal the generator wrote (values never hold a comma)."""
    return [item.strip() for item in re.split(r', (?=")', text)]


def py_literal(value: Any) -> str:
    if value is None:
        return "None"
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, int):
        return str(value)
    return json.dumps(value, ensure_ascii=False)


# ---- Types: JSON Schema -> TypedDict ---------------------------------------------------------------


class Types:
    """Renders JSON Schemas as Python types, registering a TypedDict for each object it meets."""

    def __init__(self, schemas: Dict[str, Any]):
        self.schemas = schemas
        self.blocks: Dict[str, str] = {}  # python name -> code
        self.aliases: Dict[str, str] = {}  # python name -> code (emitted after the classes)
        self.component_names: Dict[str, str] = {}
        self.reserved: set = set()

    # -- names
    def claim(self, wanted: str, exact: bool = False) -> str:
        name = re.sub(r"\W", "_", wanted)
        if name[0].isdigit():
            name = f"_{name}"
        if exact:
            if name in self.reserved:
                raise GenerationError(f"two types would be called {name}")
            self.reserved.add(name)
            return name
        candidate, n = name, 2
        while candidate in self.reserved:
            candidate, n = f"{name}{n}", n + 1
        self.reserved.add(candidate)
        return candidate

    def resolve(self, schema: Any) -> Any:
        seen = 0
        while isinstance(schema, dict) and "$ref" in schema and seen < 20:
            schema = self.schemas.get(schema["$ref"].split("/")[-1], {})
            seen += 1
        return schema

    def ref(self, component: str, quote: bool) -> str:
        if component not in self.schemas:
            raise GenerationError(f"$ref to a schema that does not exist: {component}")
        if component not in self.component_names:
            name = self.claim(pascal(component) if not component.isidentifier() else component, exact=True)
            self.component_names[component] = name
            schema = self.schemas[component]
            if self.object_properties(schema) is not None:
                self.typed_dict(name, schema, claimed=True)
            else:
                self.aliases[name] = f"{name} = {self.render(schema, name, quote=True)}"
        name = self.component_names[component]
        return f'"{name}"' if quote else name

    # -- objects
    def object_properties(self, schema: Any) -> Optional[Tuple[Dict[str, Any], List[str]]]:
        """The properties and required keys of an object schema (allOf merged), or None."""
        schema = self.resolve(schema)
        if not isinstance(schema, dict):
            return None
        if "allOf" in schema:
            props: Dict[str, Any] = {}
            required: List[str] = []
            for part in schema["allOf"]:
                found = self.object_properties(part)
                if found is None:
                    return None
                props.update(found[0])
                required += found[1]
            props.update(schema.get("properties", {}))
            required += schema.get("required", [])
            return (props, required) if props else None
        types = schema.get("type")
        if schema.get("properties") and (types in (None, "object") or (isinstance(types, list) and "object" in types and len(types) == 1)):
            return schema["properties"], list(schema.get("required", []))
        return None

    def typed_dict(self, wanted: str, schema: Any, claimed: bool = False, extra: Optional[Dict[str, Tuple[str, bool]]] = None) -> str:
        found = self.object_properties(schema)
        props, required = found if found else ({}, [])
        name = wanted if claimed else self.claim(wanted)
        self.blocks[name] = ""  # reserve the place: a cycle refers to the name before it is rendered
        fields: List[Tuple[str, str, bool]] = []
        for key, prop in props.items():
            fields.append((key, self.render(prop, name + pascal(key), quote=False), key in required))
        for key, (type_text, is_required) in (extra or {}).items():
            if key not in props:
                fields.append((key, type_text, is_required))
        self.blocks[name] = self.render_typed_dict(name, fields)
        return name

    def typed_dict_from_fields(self, wanted: str, fields: List[Tuple[str, str, bool]], exact: bool = False) -> str:
        name = self.claim(wanted, exact=exact)
        self.blocks[name] = self.render_typed_dict(name, fields)
        return name

    @staticmethod
    def render_typed_dict(name: str, fields: List[Tuple[str, str, bool]]) -> str:
        if not fields:
            return f"{name} = Dict[str, Any]"
        if all(is_identifier(key) for key, _, _ in fields):
            total = any(req for _, _, req in fields)
            head = f"class {name}(TypedDict):" if total else f"class {name}(TypedDict, total=False):"
            lines = [head]
            for key, type_text, req in fields:
                lines.append(f"    {key}: {type_text if req or not total else f'NotRequired[{type_text}]'}")
            return "\n".join(lines)
        # A key that is not a Python name: the functional syntax, whose values run at import time.
        total = all(req for _, _, req in fields)
        items = ", ".join(f"{json.dumps(key, ensure_ascii=False)}: {quote_names(t)}" for key, t, _ in fields)
        return f'{name} = TypedDict("{name}", {{{items}}}, total={total})'

    # -- any schema
    def render(self, schema: Any, context: str, quote: bool) -> str:
        if not isinstance(schema, dict) or not schema:
            return "Any"
        if "$ref" in schema:
            return self.ref(schema["$ref"].split("/")[-1], quote)
        if "const" in schema:
            return self.literal([schema["const"]])
        if isinstance(schema.get("enum"), list):
            return self.literal(schema["enum"])
        if "allOf" in schema:
            if len(schema["allOf"]) == 1 and not schema.get("properties"):
                return self.render(schema["allOf"][0], context, quote)
            if self.object_properties(schema) is not None:
                return self.object_type(schema, context, quote)
            return "Any"
        variants = schema.get("anyOf") or schema.get("oneOf")
        if isinstance(variants, list):
            return union([self.render(v, f"{context}Variant{i + 1}" if i else context, quote) for i, v in enumerate(variants)])
        types = schema.get("type")
        if types is None:
            types = ["object"] if schema.get("properties") else []
        elif not isinstance(types, list):
            types = [types]
        if not types:
            return "Any"
        rendered = []
        for t in types:
            if t == "string":
                rendered.append("str")
            elif t == "integer":
                rendered.append("int")
            elif t == "number":
                rendered.append("float")
            elif t == "boolean":
                rendered.append("bool")
            elif t == "null":
                rendered.append("None")
            elif t == "array":
                items = schema.get("items")
                rendered.append(f"List[{self.render(items, context + 'Item', quote) if items else 'Any'}]")
            elif t == "object":
                rendered.append(self.object_type(schema, context, quote))
            else:
                rendered.append("Any")
        return union(rendered)

    def object_type(self, schema: Dict[str, Any], context: str, quote: bool) -> str:
        if self.object_properties(schema) is not None:
            name = self.typed_dict(context, schema)
            return f'"{name}"' if quote else name
        extra = schema.get("additionalProperties")
        if isinstance(extra, dict) and extra:
            return f"Dict[str, {self.render(extra, context + 'Value', quote)}]"
        return "Dict[str, Any]"

    @staticmethod
    def literal(values: List[Any]) -> str:
        if any(isinstance(v, float) for v in values) or any(isinstance(v, (dict, list)) for v in values):
            return "Any"
        concrete = [v for v in values if v is not None]
        parts = [f"Literal[{', '.join(py_literal(v) for v in concrete)}]"] if concrete else []
        if any(v is None for v in values):
            parts.append("None")
        return union(parts) if parts else "None"

    # -- events: types inferred from an example, with the schema as a hint
    def from_example(self, value: Any, hint: Any, context: str) -> str:
        hint = self.resolve(hint) if isinstance(hint, dict) else None
        if hint and ("enum" in hint or "const" in hint):
            return self.render(hint, context, quote=False)
        if value is None:
            return self.render(hint, context, quote=False) if hint and (hint.get("type") or hint.get("anyOf") or hint.get("oneOf")) else "Any"
        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "str"
        if isinstance(value, list):
            items_hint = (hint or {}).get("items")
            if not value:
                return f"List[{self.render(items_hint, context + 'Item', quote=False)}]" if items_hint else "List[Any]"
            return f"List[{self.from_example(value[0], items_hint, context + 'Item')}]"
        if isinstance(value, dict):
            found = self.object_properties(hint) if hint else None
            hint_props = found[0] if found else {}
            if not value and not hint_props:
                return "Dict[str, Any]"
            name = self.claim(context)
            self.blocks[name] = ""
            fields = [(k, self.from_example(v, hint_props.get(k), name + pascal(k)), True) for k, v in value.items()]
            for k, prop in hint_props.items():
                if k not in value:
                    fields.append((k, self.render(prop, name + pascal(k), quote=False), False))
            self.blocks[name] = self.render_typed_dict(name, fields)
            return name
        return "Any"


def union(types: List[str]) -> str:
    unique: List[str] = []
    for t in types:
        inner = t[6:-1] if t.startswith("Union[") and t.endswith("]") and t.count("[") == 1 else None
        for part in ([p.strip() for p in inner.split(",")] if inner else [t]):
            if part not in unique:
                unique.append(part)
    if "Any" in unique:
        return "Any"
    has_none = "None" in unique
    rest = [t for t in unique if t != "None"]
    # `str` already holds any string literal (the spec says "a string, or the empty string").
    if "str" in rest:
        rest = [t for t in rest if not t.startswith('Literal["')]
    if not rest:
        return "None"
    if len(rest) == 1:
        return f"Optional[{rest[0]}]" if has_none else rest[0]
    return f"Union[{', '.join(rest + (['None'] if has_none else []))}]"


def quote_names(type_text: str) -> str:
    """Quotes the generated class names of a type expression that runs at import time."""
    builtin = {"Any", "Dict", "List", "Literal", "Optional", "Union", "None", "str", "int", "float", "bool"}
    out = []
    for token in re.split(r'("[^"]*"|[\[\], ])', type_text):
        out.append(f'"{token}"' if re.fullmatch(r"[A-Z_][A-Za-z0-9_]*", token or "") and token not in builtin else token)
    return "".join(out)


# ---- Operations ------------------------------------------------------------------------------------


class Operation:
    def __init__(self, merged: Dict[str, Any], op_label: str):
        method, _, path = op_label.partition(" ")
        item = merged["paths"].get(path)
        if not item or method.lower() not in item:
            raise GenerationError(f"spec/resources.json: `{op_label}` is not an operation of the spec.")
        self.method = method.upper()
        self.path = path
        self.op = item[method.lower()]
        params: Dict[Tuple[str, str], Any] = {}
        for p in item.get("parameters", []) + self.op.get("parameters", []):
            p = resolve_parameter(merged, p)
            params[(p.get("name"), p.get("in"))] = p
        self.parameters = list(params.values())
        self.path_names = re.findall(r"\{([^}]+)\}", path)

    @property
    def permission(self) -> Optional[str]:
        return self.op.get("x-fc-permission")

    def query_parameters(self) -> List[Dict[str, Any]]:
        return [p for p in self.parameters if p.get("in") == "query"]

    def header_parameters(self) -> List[Dict[str, Any]]:
        return [p for p in self.parameters if p.get("in") == "header"]

    def body(self) -> Tuple[Optional[str], Any, bool]:
        """(content type, schema, required) of the request body."""
        body = self.op.get("requestBody")
        if not body:
            return None, None, False
        content = body.get("content", {})
        for content_type in ("application/json", "multipart/form-data", "application/x-www-form-urlencoded"):
            if content_type in content:
                return content_type, content[content_type].get("schema", {}), bool(body.get("required"))
        return next(iter(content), None), None, bool(body.get("required"))

    def success_schemas(self) -> List[Any]:
        out = []
        for code, response in sorted(self.op.get("responses", {}).items()):
            if not str(code).startswith("2"):
                continue
            schema = response.get("content", {}).get("application/json", {}).get("schema")
            out.append(schema)  # None: no body (a 204)
        return out


def resolve_parameter(merged: Dict[str, Any], parameter: Dict[str, Any]) -> Dict[str, Any]:
    if "$ref" in parameter:
        return merged.get("components", {}).get("parameters", {}).get(parameter["$ref"].split("/")[-1], {})
    return parameter


# ---- Step 3: the route table and the event catalog ---------------------------------------------------


def header(spec_hash: str) -> str:
    return (
        f'"""GENERATED FILE — do not edit. Run `python scripts/generate.py`.\n\n'
        f"Source: spec/funnelchat.json (sha256 {spec_hash[:16]}…) + spec/pending.json + spec/resources.json.\n"
        f'"""\n'
    )


def event_status(post: Dict[str, Any]) -> str:
    status = post.get("x-fc-status")
    if status in ("planned", "live"):
        return status
    if status == "active":
        return "live"
    return "planned" if re.search(r"planificad", post.get("summary", ""), re.I) else "live"


def collect_events(merged: Dict[str, Any]) -> List[Dict[str, Any]]:
    by_type: Dict[str, Dict[str, Any]] = {}
    for key, item in merged.get("webhooks", {}).items():
        event_type = event_type_of_key(key)
        post = item.get("post", {})
        content = post.get("requestBody", {}).get("content", {}).get("application/json", {})
        entry = by_type.setdefault(
            event_type,
            {
                "type": event_type,
                "domains": [],
                "status": event_status(post),
                "pending": bool(post.get("x-fc-pending")),
                "data_schema": (content.get("schema") or {}).get("properties", {}).get("data"),
                "data_example": (content.get("example") or {}).get("data"),
            },
        )
        domain = post.get("x-fc-domain")
        if domain and domain not in entry["domains"]:
            entry["domains"].append(domain)
    return sorted(by_type.values(), key=lambda e: e["type"])


def generate_routes(merged: Dict[str, Any], events: List[Dict[str, Any]], spec_hash: str) -> str:
    rows = []
    for path, item in merged["paths"].items():
        for method in HTTP_METHODS:
            op = item.get(method)
            if op:
                rows.append((path, method.upper(), op))
    rows.sort(key=lambda r: (r[0], r[1]))

    def s(value: Any) -> str:
        return "None" if value is None else json.dumps(value, ensure_ascii=False)

    lines = [
        header(spec_hash),
        "from typing import NamedTuple, Optional, Tuple",
        "",
        "",
        "class Route(NamedTuple):",
        '    """One operation of the public API. `pending`: taken from spec/pending.json, not from the spec."""',
        "",
        "    method: str",
        "    path: str",
        "    operation_id: Optional[str]",
        "    domain: Optional[str]",
        "    permission: Optional[str]",
        "    pending: bool",
        "",
        "",
        "class WebhookEventInfo(NamedTuple):",
        '    """One event of the catalog. `status`: `live` is emitted today; `planned` can be subscribed to, but nothing is emitted yet."""',
        "",
        "    type: str",
        "    domains: Tuple[str, ...]",
        "    status: str",
        "    pending: bool",
        "",
        "",
        f"#: Every operation of the spec ({len(rows)}), sorted by path.",
        "ROUTES: Tuple[Route, ...] = (",
    ]
    for path, method, op in rows:
        lines.append(
            f"    Route({s(method)}, {s(path)}, {s(op.get('operationId'))}, {s(op.get('x-fc-domain'))}, "
            f"{s(op.get('x-fc-permission'))}, {bool(op.get('x-fc-pending'))}),"
        )
    lines += [")", "", f"#: Every webhook event type the spec knows ({len(events)}).", "WEBHOOK_EVENTS: Tuple[WebhookEventInfo, ...] = ("]
    for e in events:
        domains = "(" + "".join(f"{s(d)}, " for d in e["domains"]).rstrip(" ") + ")" if e["domains"] else "()"
        lines.append(f"    WebhookEventInfo({s(e['type'])}, {domains}, {s(e['status'])}, {e['pending']}),")
    lines += [")", ""]
    return "\n".join(lines)


# ---- Steps 4 and 5: types and resources -----------------------------------------------------------


# What every event carries and the spec does not describe yet (funnelchat-node keeps it in
# src/pending/events.ts): the workspace of the event, in production since accounts v1.5.97
# (558332bcf, 04-11-2026, Webhook/Services/EventWorkspaceRouting.php:65-85). `None` only for an
# account with no workspace at all. When the spec describes it, it stops being added.
PENDING_COMMON_EVENT_DATA = {"workspace_id": ("Optional[int]", True)}


def wrap_doc(text: str, indent: str, width: int = 100) -> List[str]:
    lines: List[str] = []
    for paragraph in text.replace('"""', "'''").replace("\\", "\\\\").split("\n\n"):
        wrapped = textwrap.wrap(" ".join(paragraph.split()), width=width - len(indent), break_long_words=False, break_on_hyphens=False)
        if lines:
            lines.append("")
        lines += [f"{indent}{line}" if line else "" for line in wrapped]
    return lines


def docstring(text: str, indent: str) -> List[str]:
    body = wrap_doc(text, indent)
    if len(body) == 1 and len(body[0]) + 6 <= 100:
        return [f'{indent}"""{body[0].strip()}"""']
    return [f'{indent}"""{body[0].strip()}', *body[1:], f'{indent}"""']


class MethodSpec:
    def __init__(self, resource: Dict[str, Any], method: Dict[str, Any], operation: Operation, types: Types):
        self.resource = resource
        self.method = method
        self.operation = operation
        self.types = types
        self.name = method["name"]
        self.context = resource["class"] + pascal(self.name)
        self.is_send = operation.method == "POST" and (operation.permission or "").endswith(":send")
        self.warnings: List[str] = []

    def build(self) -> str:
        op = self.operation
        where = f"{self.resource['class']}.{self.name} ({op.method} {op.path})"
        path_names = self.method.get("pathNames", {})
        path_params = [(spec_name, path_names.get(spec_name, snake(spec_name))) for spec_name in op.path_names]
        for spec_name, _ in path_params:
            if not any(p.get("name") == spec_name and p.get("in") == "path" for p in op.parameters):
                self.warnings.append(f"{where}: the path parameter {spec_name} is not declared in the spec")
        path_types = {}
        for p in op.parameters:
            if p.get("in") == "path":
                rendered = self.types.render(p.get("schema"), self.context + pascal(p["name"]), quote=False)
                path_types[p["name"]] = "Union[int, str]" if rendered == "Any" else rendered

        # (wire key, python name, kind, type, required). A Laravel array, `tag_ids[]`, is the keyword
        # `tag_ids`: the query serializer writes a list as `tag_ids[]=…`. A Python keyword gets a `_`.
        keywords: List[Tuple[str, str, str, str, bool]] = []
        if self.method.get("query", True) is not False:
            for p in op.query_parameters():
                wire = p["name"][:-2] if p["name"].endswith("[]") else p["name"]
                type_text = self.types.render(p.get("schema"), self.context + "Query" + pascal(wire), quote=False)
                keywords.append((wire, python_name(wire), "query", type_text, bool(p.get("required"))))
        content_type, body_schema, body_required = op.body()
        body_param: Optional[str] = None
        defaults = self.method.get("bodyDefaults", {})
        if content_type is not None:
            found = self.types.object_properties(body_schema) if body_schema is not None else None
            if content_type == "application/json" and found is not None:
                props, required = found
                base = self.context + "Body"
                if isinstance(body_schema, dict) and "$ref" in body_schema:
                    base = self.types.ref(body_schema["$ref"].split("/")[-1], quote=False)
                for key, prop in props.items():
                    type_text = self.types.render(prop, base + pascal(key), quote=False)
                    keywords.append((key, python_name(key), "body", type_text, key in required and key not in defaults))
            else:
                body_param = self.types.render(body_schema, self.context + "Body", quote=False) if body_schema else "Any"
                if content_type != "application/json":
                    self.warnings.append(f"{where}: a {content_type} body is sent as JSON; pass it in `body`")

        taken = {python for _, python in path_params} | {"self"}
        accepted: List[Tuple[str, str, str, str, bool]] = []
        skipped: List[str] = []
        for wire, python, kind, type_text, required in keywords:
            if python is None or python in REQUEST_OPTIONS or python in taken:
                skipped.append(f"`{wire}`")
                if required:
                    raise GenerationError(f"{where}: the required field `{wire}` cannot be a keyword argument")
                continue
            taken.add(python)
            accepted.append((wire, python, kind, type_text, required))
        if skipped:
            self.warnings.append(f"{where}: {', '.join(skipped)} only through extra_query / extra_body")

        has_query = any(kind == "query" for _, _, kind, _, _ in accepted) or self.method.get("paginate") or op.method in ("GET", "DELETE")
        has_body = content_type is not None
        idempotent = bool(self.method.get("idempotent"))
        if idempotent and not any(p.get("name", "").lower() == "idempotency-key" for p in op.header_parameters()):
            self.warnings.append(f"{where}: `idempotency_key` is not declared in the spec (sent anyway)")

        # Signature
        sig = ["        self,"]
        for spec_name, python in path_params:
            sig.append(f"        {python}: {path_types.get(spec_name, 'Union[int, str]')},")
        if path_params:
            sig.append("        /,")
        if body_param is not None:
            sig.append(f"        body: {body_param}{'' if body_required else ' | None = None'},")
        rest = []
        for _, python, _, type_text, required in sorted(accepted, key=lambda k: not k[4]):
            rest.append(f"        {python}: {type_text}," if required else f"        {python}: {type_text} | NotGiven = NOT_GIVEN,")
        if idempotent:
            rest.append("        idempotency_key: Optional[str] = None,")
        if has_query:
            rest.append("        extra_query: Optional[Dict[str, Any]] = None,")
        if has_body and body_param is None:
            rest.append("        extra_body: Optional[Dict[str, Any]] = None,")
        rest.append("        extra_headers: Optional[Dict[str, str]] = None,")
        rest.append("        timeout: Optional[float] = None,")
        rest.append("        max_retries: Optional[int] = None,")
        if self.is_send:
            rest.append("        retry_send: bool = False,")
        sig += ["        *,"] + rest if not path_params or rest else []

        returns = self.return_type()
        lines = [f"    def {self.name}(", *sig, f"    ) -> {returns}:"]
        doc = self.method["doc"]
        if op.permission:
            doc += f"\n\nPermission: **{PERMISSION_NAMES.get(op.permission, 'not named in the panel')}**."
        if skipped:
            doc += f"\n\nOther fields ({', '.join(skipped)}): pass them in `extra_query` or `extra_body`."
        lines += docstring(doc, "        ")

        # Body of the method
        call = "_paginate" if self.method.get("paginate") else "_request"
        args = [] if self.method.get("paginate") else [f'"{op.method}"']
        args.append(json.dumps(op.path))
        if path_params:
            args.append("path_params={" + ", ".join(f'"{s}": {p}' for s, p in path_params) + "}")
        query_items = [(wire, python) for wire, python, kind, _, _ in accepted if kind == "query"]
        body_items = []
        for wire, python, kind, _, _ in accepted:
            if kind != "body":
                continue
            if wire in defaults:
                path_python = dict(path_params)[defaults[wire]]
                body_items.append((wire, f"{path_python} if {python} is NOT_GIVEN else {python}"))
            else:
                body_items.append((wire, python))
        if query_items:
            args.append("query={" + ", ".join(f'"{k}": {v}' for k, v in query_items) + "}")
        if body_param is not None:
            args.append("body=body")
        elif body_items:
            args.append("body={" + ", ".join(f'"{k}": {v}' for k, v in body_items) + "}")
        elif has_body:
            args.append("body={}")
        for option, present in (
            ("idempotency_key", idempotent),
            ("extra_query", has_query),
            ("extra_body", has_body and body_param is None),
            ("extra_headers", True),
            ("timeout", True),
            ("max_retries", True),
            ("retry_send", self.is_send),
        ):
            if present:
                args.append(f"{option}={option}")
        # `_request` returns the decoded JSON as Any: the cast states what the spec says it is.
        cast_open, cast_close = ("", "") if call == "_paginate" or returns == "Any" else (f'cast("{returns}", ', ")")
        one_line = f"        return {cast_open}self.{call}({', '.join(args)}){cast_close}"
        if len(one_line) <= 100:
            lines.append(one_line)
        else:
            lines.append(f"        return {cast_open}self.{call}(")
            for arg in args:
                if len(arg) + 13 > 100 and arg.endswith("}") and "={" in arg:
                    name, _, items = arg.partition("={")
                    lines.append(f"            {name}={{")
                    lines += [f"                {item}," for item in split_items(items[:-1])]
                    lines.append("            },")
                else:
                    lines.append(f"            {arg},")
            lines.append(f"        ){cast_close}")
        return "\n".join(lines)

    def return_type(self) -> str:
        schemas = self.operation.success_schemas()
        if self.method.get("paginate"):
            item = None
            for schema in schemas:
                item = self.list_item(schema)
                if item is not None:
                    break
            if item is None:
                self.warnings.append(f"{self.resource['class']}.{self.name}: no list in the response; items typed Any")
                return "Page[Any]"
            return f"Page[{self.types.render(item, self.context + 'Item', quote=False)}]"
        rendered: List[str] = []
        seen: List[str] = []
        for schema in schemas:
            key = canonical(schema)
            if key in seen:
                continue
            seen.append(key)
            rendered.append("None" if schema is None else self.types.render(schema, self.context + "Response", quote=False))
        return union(rendered) if rendered else "Any"

    def list_item(self, schema: Any) -> Any:
        schema = self.types.resolve(schema)
        if not isinstance(schema, dict):
            return None
        for variant in schema.get("anyOf") or schema.get("oneOf") or []:
            found = self.list_item(variant)
            if found is not None:
                return found
        types = schema.get("type")
        if types == "array" or (isinstance(types, list) and "array" in types):
            return schema.get("items", {})
        found = self.types.object_properties(schema)
        if found and "data" in found[0]:
            data = self.types.resolve(found[0]["data"])
            if isinstance(data, dict) and (data.get("type") == "array" or "items" in data):
                return data.get("items", {})
        return None


def generate_types_and_resources(
    merged: Dict[str, Any], manifest: Dict[str, Any], events: List[Dict[str, Any]], spec_hash: str
) -> Tuple[str, str, List[str]]:
    types = Types(merged["components"]["schemas"])
    warnings: List[str] = []
    resource_blocks: List[str] = []
    resources = manifest["resources"]
    for name in [r["class"] for r in resources] + ["ClientResources", "Page", "NotGiven", "Resource"]:
        types.reserved.add(name)

    for resource in resources:
        mixins = []
        for mixin in resource.get("mixins", []):
            mixins.append(mixin.split(":")[1])
        lines = [f"class {resource['class']}({', '.join(['Resource'] + mixins)}):"]
        lines += docstring(resource["doc"], "    ")
        for method in resource["methods"]:
            spec = MethodSpec(resource, method, Operation(merged, method["op"]), types)
            lines += ["", spec.build()]
            warnings += spec.warnings
        resource_blocks.append("\n".join(lines))

    # Events: one TypedDict per type, discriminated by `type`.
    event_names: List[str] = []
    for e in events:
        base = pascal(e["type"].replace(".", "_"))
        schema, example = e["data_schema"], e["data_example"]
        explicit = bool(schema and types.object_properties(schema) is not None and isinstance(types.resolve(schema).get("required"), list))
        data_name = f"{base}EventData"
        if explicit:
            data_type = types.typed_dict(types.claim(data_name, exact=True), schema, claimed=True, extra=PENDING_COMMON_EVENT_DATA)
        elif isinstance(example, dict):
            data_type = types.from_example(example, schema, data_name)
            block = types.blocks.get(data_type, "")
            if block.startswith("class ") and "workspace_id:" not in block:
                types.blocks[data_type] = block + "\n    workspace_id: Optional[int]"
        elif schema:
            data_type = types.render(schema, data_name, quote=False)
        else:
            data_type = "Dict[str, Any]"
        event_names.append(
            types.typed_dict_from_fields(
                f"{base}Event",
                [("id", "str", True), ("type", f"Literal[{py_literal(e['type'])}]", True), ("version", "int", True), ("occurred_at", "str", True), ("data", data_type, True)],
                exact=True,
            )
        )

    used_in_resources = sorted(
        {n for block in resource_blocks for n in re.findall(r"\b[A-Z][A-Za-z0-9_]*\b", block) if n in types.blocks or n in types.aliases}
    )
    names = list(types.blocks) + list(types.aliases)
    types_lines = [
        header(spec_hash),
        "The shapes of what the API answers and of every webhook event, as TypedDicts: at runtime they",
        "are plain dicts (the decoded JSON), so `message[\"status\"]` and `json.dumps(message)` just work.",
        '"""',
    ]
    types_lines = [types_lines[0].rstrip('"\n') + "\n" + "\n".join(types_lines[1:])]
    types_lines += [
        "",
        "from __future__ import annotations",
        "",
        "from typing import TYPE_CHECKING, Any, Dict, List, Literal, Optional, TypedDict, Union",
        "",
        "if TYPE_CHECKING:",
        "    from typing_extensions import NotRequired",
        "",
        "__all__ = [",
        *[f'    "{n}",' for n in sorted(names + ["WebhookEvent", "WebhookEventType"])],
        "]",
    ]
    for name, block in types.blocks.items():
        types_lines += ["", "", block]
    for name, alias in types.aliases.items():
        types_lines += ["", "", alias]
    types_lines += [
        "",
        "",
        "#: Every webhook event type the spec knows.",
        "WebhookEventType = Literal[",
        *[f"    {py_literal(e['type'])}," for e in events],
        "]",
        "",
        "#: A verified webhook event, discriminated by `type`. New types can arrive before this SDK",
        "#: knows them: answer 2xx to the ones you do not handle.",
        "WebhookEvent = Union[",
        *[f'    "{n}",' for n in event_names],
        "]",
        "",
    ]

    resources_lines = [
        header(spec_hash).rstrip('"\n') + "\n\nThe resources of the client: one class per piece of the API, from spec/resources.json.\n\"\"\"",
        "",
        "from __future__ import annotations",
        "",
        "from typing import TYPE_CHECKING, Any, Dict, List, Literal, Optional, Union, cast",
        "",
        "from ._resource import NOT_GIVEN, NotGiven, Resource",
    ]
    for module in sorted({m.split(":")[0] for r in resources for m in r.get("mixins", [])}):
        classes = sorted({m.split(":")[1] for r in resources for m in r.get("mixins", []) if m.split(":")[0] == module})
        relative = "." + module.split(".", 1)[1] if module.startswith("funnelchat.") else module
        resources_lines.append(f"from {relative} import {', '.join(classes)}")
    resources_lines += ["", "if TYPE_CHECKING:", "    from ._client import Funnelchat", "    from ._pagination import Page"]
    if used_in_resources:
        resources_lines.append("    from .types import (")
        resources_lines += [f"        {n}," for n in used_in_resources]
        resources_lines.append("    )")
    resources_lines += ["", "__all__ = [", *[f'    "{r["class"]}",' for r in resources], '    "ClientResources",', "]"]
    for block in resource_blocks:
        resources_lines += ["", "", block]
    resources_lines += [
        "",
        "",
        "class ClientResources:",
        '    """The resources of `Funnelchat`, one attribute each."""',
        "",
        *[f"    {r['attribute']}: {r['class']}" for r in resources],
        "",
        "    def _init_resources(self) -> None:",
        '        client = cast("Funnelchat", self)',
        *[f"        self.{r['attribute']} = {r['class']}(client)" for r in resources],
        "",
    ]
    return "\n".join(types_lines), "\n".join(resources_lines), warnings


# ---- Main ------------------------------------------------------------------------------------------


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    if args.spec:
        import_spec(args.spec, args.declared, args.domains, args.expect_sha256)
    if args.pending:
        import_pending(args.pending)
    if not SPEC_FILE.exists():
        raise GenerationError("Missing spec/funnelchat.json: run `python scripts/generate.py --spec <file>`.")

    data = SPEC_FILE.read_bytes()
    spec_hash = sha256(data)
    provenance = read_provenance()
    if provenance.get("sha256") and provenance["sha256"] != spec_hash:
        print("warning: spec/funnelchat.json does not match the sha256 in spec/procedencia.json (was it edited by hand?).", file=sys.stderr)
    pending_bytes = PENDING_FILE.read_bytes() if PENDING_FILE.exists() else b"{}"
    if provenance.get("pending", {}).get("sha256") not in (None, sha256(pending_bytes)):
        print("warning: spec/pending.json does not match the sha256 in spec/procedencia.json (was it edited here?).", file=sys.stderr)

    spec = json.loads(data.decode("utf-8"))
    pending = json.loads(pending_bytes.decode("utf-8"))
    manifest = json.loads(RESOURCES_FILE.read_text("utf-8"))
    merged, report = merge_pending(spec, pending)
    events = collect_events(merged)

    types_py, resources_py, warnings = generate_types_and_resources(merged, manifest, events, spec_hash)
    files = {
        "_routes.py": generate_routes(merged, events, spec_hash),
        "types.py": types_py,
        "resources.py": resources_py,
    }
    assert_permission_names(files)

    print(f"pending of the spec: {len(report['applied'])} entries applied.")
    if report["superseded"]:
        print(f"the spec already has {len(report['superseded'])} entries of spec/pending.json; they can be deleted from it (in funnelchat-node):")
        for label in report["superseded"]:
            print(f"  - {label}")
    if report["missing"]:
        print(f"warning: {len(report['missing'])} patches did not find their operation in the spec:", file=sys.stderr)
        for label in report["missing"]:
            print(f"  - {label}", file=sys.stderr)
    for warning in warnings:
        print(f"note: {warning}")

    if args.check:
        stale = [name for name, content in files.items() if not (PACKAGE / name).exists() or (PACKAGE / name).read_text("utf-8") != content]
        if stale:
            print(f"src/funnelchat is out of date ({', '.join(stale)}): run `python scripts/generate.py`.", file=sys.stderr)
            return 1
        print("src/funnelchat is up to date.")
        return 0

    for name, content in files.items():
        (PACKAGE / name).write_text(content, "utf-8")
    print("generated: " + ", ".join(f"src/funnelchat/{n}" for n in files))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except GenerationError as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
