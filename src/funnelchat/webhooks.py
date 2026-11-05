"""Verification of the webhook deliveries (`X-Funnelchat-Signature`), without a client or a key.

It replicates the algorithm of the developer portal (`snippets/verificar_firma.py`), the same as
funnelchat-node and funnelchat-php:

    X-Funnelchat-Signature: t=<unix>,v1=<hex(hmac_sha256(secret, "<t>." + raw body))>

- the header is split by `,` and each part by its first `=`; keys and values are trimmed;
- `t` must be digits only; there can be several `v1` (any match is enough);
- a `t` farther than `tolerance_seconds` (300 by default) from the local clock is rejected;
- the HMAC uses the full secret as shown (the `whsec_` prefix is part of it) over the raw bytes of
  the body, compared in constant time.

    event = funnelchat.webhooks.construct_event(raw_body, signature_header, secret)
    if event["type"] == "message.status_changed" and event["data"]["status"] == "read":
        ...
"""

from __future__ import annotations

import hashlib
import hmac
import json
import re
import time
from typing import TYPE_CHECKING, Optional, Tuple, Union, cast

from ._errors import WebhookVerificationError

if TYPE_CHECKING:
    from .types import WebhookEvent

__all__ = [
    "SIGNATURE_HEADER",
    "DEFAULT_TOLERANCE_SECONDS",
    "verify",
    "construct_event",
    "WebhookHelpers",
    "WebhookVerificationError",
]

#: The name of the signature header.
SIGNATURE_HEADER = "X-Funnelchat-Signature"
#: Default tolerance between `t` and the local clock, in seconds.
DEFAULT_TOLERANCE_SECONDS = 300

#: The body exactly as it arrived: never parsed and serialized again.
RawBody = Union[bytes, bytearray, memoryview, str]


def _check(
    payload: object, signature_header: object, secret: object, tolerance_seconds: float
) -> Optional[Tuple[str, str]]:
    """None when the delivery is authentic and recent; otherwise (reason, message)."""
    if not isinstance(secret, str) or not secret:
        return "missing_secret", "Missing the subscription secret."
    if isinstance(payload, str):
        body = payload.encode("utf-8")
    elif isinstance(payload, (bytes, bytearray, memoryview)):
        body = bytes(payload)
    else:
        return (
            "invalid_body",
            "The body must be the raw one (bytes or str), exactly as it arrived: with Flask "
            "`request.get_data()`, with FastAPI `await request.body()`, with Django `request.body`.",
        )
    if not isinstance(signature_header, str) or not signature_header:
        return "missing_header", f"Missing the {SIGNATURE_HEADER} header."

    t: Optional[str] = None
    signatures = []
    for part in signature_header.split(","):
        key, sep, value = part.partition("=")
        if not sep:
            continue
        key, value = key.strip(), value.strip()
        if key == "t":
            t = value
        elif key == "v1":
            signatures.append(value)
    if t is None or not re.fullmatch(r"[0-9]+", t) or not signatures:
        return "malformed_header", f"The {SIGNATURE_HEADER} header is not t=<unix>,v1=<hex>."

    if abs(int(time.time()) - int(t)) > tolerance_seconds:
        return "timestamp_out_of_tolerance", f"The signature is more than {tolerance_seconds:g} seconds away from the local clock."

    expected = hmac.new(secret.encode("utf-8"), f"{t}.".encode("ascii") + body, hashlib.sha256).hexdigest()
    if any(hmac.compare_digest(candidate.encode("utf-8"), expected.encode("ascii")) for candidate in signatures):
        return None
    return "signature_mismatch", "The signature does not match the body and the secret."


def verify(
    payload: RawBody,
    signature_header: Optional[str],
    secret: str,
    *,
    tolerance_seconds: float = DEFAULT_TOLERANCE_SECONDS,
) -> bool:
    """True when the delivery is authentic and recent. It never raises: any problem is False. Use
    `construct_event()` to know which check failed."""
    return _check(payload, signature_header, secret, tolerance_seconds) is None


def construct_event(
    payload: RawBody,
    signature_header: Optional[str],
    secret: str,
    *,
    tolerance_seconds: float = DEFAULT_TOLERANCE_SECONDS,
) -> "WebhookEvent":
    """Verifies the signature and returns the event (`id`, `type`, `version`, `occurred_at`,
    `data`). Raises WebhookVerificationError, with `reason`, when the signature, the timestamp or
    the body are not valid. Pass the raw body as it arrived, never one parsed and serialized again.

    New event types can arrive before this SDK knows them: answer 2xx to the ones you do not handle.
    """
    failure = _check(payload, signature_header, secret, tolerance_seconds)
    if failure is not None:
        raise WebhookVerificationError(*failure)
    text = payload if isinstance(payload, str) else bytes(payload).decode("utf-8", errors="replace")
    try:
        event = json.loads(text)
    except ValueError:
        raise WebhookVerificationError("invalid_json", "The signature is valid but the body is not JSON.") from None
    if not (isinstance(event, dict) and isinstance(event.get("id"), str) and isinstance(event.get("type"), str) and "data" in event):
        raise WebhookVerificationError("invalid_event", "The signature is valid but the body is not an event (id, type, data).")
    return cast("WebhookEvent", event)


class WebhookHelpers:
    """`verify()` and `construct_event()` on `client.webhooks`, the same functions as this module's."""

    verify = staticmethod(verify)
    construct_event = staticmethod(construct_event)
