"""A handful of tests with a mocked transport: no network and no keys."""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from typing import Any, Callable, Dict, List

import httpx
import pytest

import funnelchat
from funnelchat import Funnelchat

Handler = Callable[[httpx.Request], httpx.Response]


def make_client(handler: Handler, calls: List[httpx.Request], **options: Any) -> Funnelchat:
    def record(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return handler(request)

    client = Funnelchat(
        api_key="1|fc_live_test",
        http_client=httpx.Client(transport=httpx.MockTransport(record)),
        **options,
    )
    client._sleep = lambda seconds: None  # no real waits between retries
    return client


def reply(status: int, body: Any = None, headers: Dict[str, str] | None = None) -> httpx.Response:
    return httpx.Response(status, json=body, headers={"X-Request-Id": "req-123", **(headers or {})})


def test_send_by_phone_in_one_call_and_never_retried() -> None:
    calls: List[httpx.Request] = []
    message = {"id": 1002, "contact_id": 2001, "device_id": 3, "status": "queued"}
    client = make_client(lambda request: reply(200, {"message": message}), calls)

    result = client.messages.send_direct(device_id=3, phone="5491100000000", text="Hi Ana!")

    assert result["message"]["id"] == 1002 and result["message"]["status"] == "queued"
    request = calls[0]
    assert request.method == "POST"
    assert str(request.url) == "https://api.funnelchat.com/api/v1/message/send-message"
    assert json.loads(request.content) == {"device_id": 3, "phone": "5491100000000", "text": "Hi Ana!"}
    assert request.headers["Authorization"] == "Bearer 1|fc_live_test"
    assert request.headers["User-Agent"].startswith(f"funnelchat-python/{funnelchat.__version__} python/")
    assert client.last_response is not None and client.last_response.request_id == "req-123"

    # A send that may have been applied is never repeated by the SDK, not even a 429 unless asked.
    for status, body in ((500, {"message": "Server Error"}), (429, {"error": "rate_limited"})):
        calls.clear()
        client = make_client(lambda request: reply(status, body, {"Retry-After": "0"}), calls)
        with pytest.raises(funnelchat.APIError):
            client.messages.send_direct(device_id=3, phone="5491100000000", text="Hi Ana!")
        assert len(calls) == 1
    calls.clear()
    with pytest.raises(funnelchat.RateLimitError):
        client.messages.send_direct(device_id=3, phone="5491100000000", text="Hi", retry_send=True)
    assert len(calls) == 3  # retry_send: the rule of writes, 1 + max_retries on a 429


def test_follow_a_group() -> None:
    calls: List[httpx.Request] = []
    followed = {"uid": "120363000000000001@g.us", "name": "Customers", "imported": True, "is_admin": True}
    client = make_client(lambda request: reply(201, {"data": followed}), calls)

    result = client.groups.follow("120363000000000001@g.us", device_id=3)

    assert result["data"]["imported"] is True and result["data"]["is_admin"] is True
    assert calls[0].method == "POST"
    assert calls[0].url.raw_path == b"/api/v1/groups/120363000000000001%40g.us/import"
    assert json.loads(calls[0].content) == {"device_id": 3}


def test_bring_a_numbers_templates_from_meta() -> None:
    calls: List[httpx.Request] = []
    client = make_client(lambda request: reply(202, {"status": "in_progress"}), calls)

    assert client.templates.sync(3) == {"status": "in_progress"}
    assert (calls[0].method, calls[0].url.path, calls[0].content) == ("POST", "/api/v1/devices/3/templates", b"")

    calls.clear()
    refused = {"error": "meta_rejected", "message": "Meta rejected it", "meta_code": 190}
    client = make_client(lambda request: reply(422, refused), calls)
    with pytest.raises(funnelchat.UnprocessableEntityError) as raised:
        client.templates.sync(3)
    assert (raised.value.code, raised.value.body["meta_code"], len(calls)) == ("meta_rejected", 190, 1)
    assert funnelchat.TEMPLATE_SYNC_ERROR_CODES["meta_rejected"] == 422


def test_error_mapping() -> None:
    calls: List[httpx.Request] = []
    cases = [
        (401, {"error": "unauthenticated", "message": "Unauthenticated."}, funnelchat.AuthenticationError),
        (403, {"error": "permission_denied", "message": "Missing permission"}, funnelchat.PermissionDeniedError),
        (404, {"message": "Not found"}, funnelchat.NotFoundError),
        (415, {"message": "Unsupported", "supported_file_types": ["pdf"]}, funnelchat.UnsupportedMediaTypeError),
        (422, {"error": "window_closed", "message": "Window closed"}, funnelchat.UnprocessableEntityError),
        (502, {"error": "origin_unreachable", "message": "Unreachable"}, funnelchat.InternalServerError),
    ]
    for status, body, cls in cases:
        client = make_client(lambda request: reply(status, body), calls, max_retries=0)
        with pytest.raises(cls) as raised:
            client.contacts.retrieve(2001)
        error = raised.value
        assert isinstance(error, funnelchat.APIError)
        assert (error.status, error.code, error.request_id, error.body) == (status, body.get("error"), "req-123", body)
    assert funnelchat.is_send_rule_error("window_closed") and not funnelchat.is_send_rule_error("unauthenticated")

    validation = {"message": "The phone field is required.", "errors": {"phone": ["The phone field is required."]}}
    client = make_client(lambda request: reply(422, validation), calls)
    with pytest.raises(funnelchat.UnprocessableEntityError) as raised:
        client.messages.send_direct(device_id=3, text="Hi")
    assert raised.value.code is None and raised.value.errors == validation["errors"]

    # A read is retried on a 429 with the wait it asks for; one longer than 60 s is raised right away.
    calls.clear()
    answers = iter([reply(429, {"error": "rate_limited"}, {"Retry-After": "1"}), reply(200, {"data": {"id": 2001}})])
    assert make_client(lambda request: next(answers), calls).contacts.retrieve(2001) == {"data": {"id": 2001}}
    assert len(calls) == 2
    calls.clear()
    client = make_client(lambda request: reply(429, {"error": "daily_cap_exceeded"}, {"Retry-After": "3600"}), calls)
    with pytest.raises(funnelchat.RateLimitError) as raised:
        client.contacts.retrieve(2001)
    assert raised.value.retry_after == 3600 and len(calls) == 1

    calls.clear()
    client = make_client(lambda request: (_ for _ in ()).throw(httpx.ConnectError("refused", request=request)), calls, max_retries=0)
    with pytest.raises(funnelchat.APIConnectionError):
        client.devices.list()


# The signature vectors of the developer portal (`tests/test_firmas.py`), as funnelchat-node's
# test/fixtures/portal-signature-vectors.ts replicates them. The secret is a published test value.
SECRET = "whsec_prueba_9f3a1c7e5b2d4a6c8e0f1a3b5c7d9e1f"
BODY = (
    '{"id":"evt_000000000000000000000001","type":"message.received","version":1,"occurred_at":"2026-10-01T12:00:00Z",'
    '"data":{"message":{"id":1001,"type":"text","text":"Hola, quiero más información","media":null},'
    '"contact":{"id":2001,"name":"Contacto de ejemplo","phone":"+5491100000000"},"receiver":{"phone":"+5491100000001"}}}'
).encode("utf-8")
FIXED_T = 1790856000
FIXED_V1 = "c78b061f77e36cc12c72392f1507bf147bd55c0d90848ef8dab47769607aeb44"


def sign(body: bytes, secret: str, t: int) -> str:
    return f"t={t},v1={hmac.new(secret.encode(), f'{t}.'.encode() + body, hashlib.sha256).hexdigest()}"


def test_signature_verification() -> None:
    t = int(time.time())
    ok = sign(BODY, SECRET, t)
    v1 = ok.split("v1=")[1]
    utf8_body = '{"texto":"Ñandú 🚀 — acentos: áéíóú"}'.encode("utf-8")
    bare_secret = "9f3a1c7e5b2d4a6c8e0f1a3b5c7d9e1f"
    cases = [
        (BODY, ok, SECRET, True),  # correct signature
        (BODY.replace(b"Hola", b"Hole"), ok, SECRET, False),  # body altered
        (json.dumps(json.loads(BODY), indent=2).encode(), ok, SECRET, False),  # re-serialized
        (BODY, f"t={t},v1={'1' if v1[0] == '0' else '0'}{v1[1:]}", SECRET, False),  # signature altered
        (BODY, ok, SECRET + "x", False),  # wrong secret
        (BODY, f"t={t + 1},v1={v1}", SECRET, False),  # timestamp altered
        (BODY, sign(BODY, SECRET, t - 600), SECRET, False),  # 10 minutes old
        (BODY, f"sha256={v1}", SECRET, False),  # malformed header
        (BODY, f"t={t}", SECRET, False),  # without v1
        (BODY, "", SECRET, False),  # empty header
        (utf8_body, sign(utf8_body, SECRET, t), SECRET, True),  # raw UTF-8 bytes
        (BODY, sign(BODY, bare_secret, t), bare_secret, True),  # a secret without whsec_ is used as is
        (BODY, ok, SECRET.replace("whsec_", ""), False),  # the prefix stripped by mistake
    ]
    for body, header, secret, expected in cases:
        assert funnelchat.webhooks.verify(body, header, secret) is expected, (header, secret)
    # The algorithm itself, against a vector computed independently of this SDK.
    assert funnelchat.webhooks.verify(BODY, f"t={FIXED_T},v1={FIXED_V1}", SECRET, tolerance_seconds=10**10)

    client = Funnelchat(api_key="1|fc_live_test")
    event = client.webhooks.construct_event(BODY.decode("utf-8"), ok, SECRET)
    assert event["type"] == "message.received" and event["id"] == "evt_000000000000000000000001"
    for header, reason in (("", "missing_header"), (f"t={t}", "malformed_header"), (sign(BODY, SECRET, t - 600), "timestamp_out_of_tolerance"), (f"t={t},v1=00", "signature_mismatch")):
        with pytest.raises(funnelchat.WebhookVerificationError) as raised:
            funnelchat.webhooks.construct_event(BODY, header, SECRET)
        assert raised.value.reason == reason
