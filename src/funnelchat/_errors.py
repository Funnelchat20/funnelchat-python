"""Errors raised by the SDK.

    FunnelchatError                   base class of everything the SDK raises
    ├── APIError                      the API answered with a non-2xx status
    │   ├── BadRequestError           400
    │   ├── AuthenticationError       401
    │   ├── PermissionDeniedError     403
    │   ├── NotFoundError             404
    │   ├── ConflictError             409
    │   ├── UnsupportedMediaTypeError 415
    │   ├── UnprocessableEntityError  422
    │   ├── RateLimitError            429
    │   └── InternalServerError       5xx
    ├── APIConnectionError            no response (network error)
    │   └── APIConnectionTimeoutError
    └── WebhookVerificationError      a webhook delivery failed signature verification

The same classes as funnelchat-node, with the same meaning.
"""

from __future__ import annotations

import time
from email.utils import parsedate_to_datetime
from typing import Any, Dict, List, Mapping, Optional

__all__ = [
    "FunnelchatError",
    "APIError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnsupportedMediaTypeError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "APIConnectionError",
    "APIConnectionTimeoutError",
    "WebhookVerificationError",
]


class FunnelchatError(Exception):
    """Base class of every error raised by the SDK."""


class APIError(FunnelchatError):
    """The API answered with a non-2xx status.

    - `status`: the HTTP status.
    - `code`: the stable `error` of the body (`window_closed`, `rate_limited`,
      `route_not_available`…), or `None` when the body has none (for example a validation `422`,
      which carries `errors` instead). Decide by `status` and `code`, never by `message`.
    - `message`: the `message` of the body, meant for people.
    - `request_id`: the `X-Request-Id` of the response. Quote it when you report a problem.
    - `retry_after`: the seconds of the `Retry-After` header, when present.
    - `errors`: in a validation `422`, the messages per field.
    - `body`: the decoded body (or its text when it is not JSON).
    """

    status: int
    code: Optional[str]
    message: str
    request_id: Optional[str]
    retry_after: Optional[float]
    errors: Optional[Dict[str, List[str]]]
    body: Any
    headers: Mapping[str, str]
    method: str
    url: str

    def __init__(self, *, status: int, body: Any, headers: Mapping[str, str], method: str, url: str) -> None:
        record = body if isinstance(body, dict) else {}
        code = record.get("error") if isinstance(record.get("error"), str) and record.get("error") else None
        api_message = record.get("message") if isinstance(record.get("message"), str) and record.get("message") else None
        fallback = body.strip() if isinstance(body, str) and body.strip() and len(body) <= 300 else None
        self.status = status
        self.code = code
        self.message = api_message or code or fallback or f"The API answered {status}."
        self.request_id = request_id_of(headers)
        self.retry_after = parse_retry_after(headers.get("retry-after"))
        self.errors = record.get("errors") if isinstance(record.get("errors"), dict) else None
        self.body = body
        self.headers = headers
        self.method = method
        self.url = url
        super().__init__(self.message)

    def __str__(self) -> str:
        head = f"{self.status} {self.code}" if self.code else str(self.status)
        tail = f" (request id {self.request_id})" if self.request_id else ""
        return f"{head}: {self.message}{tail}"

    @staticmethod
    def from_response(*, status: int, body: Any, headers: Mapping[str, str], method: str, url: str) -> "APIError":
        """The subclass that matches the status."""
        cls: type = APIError
        if status in _BY_STATUS:
            cls = _BY_STATUS[status]
        elif status >= 500:
            cls = InternalServerError
        error: APIError = cls(status=status, body=body, headers=headers, method=method, url=url)
        return error


class BadRequestError(APIError):
    """400."""


class AuthenticationError(APIError):
    """401: the key is missing or not valid."""


class PermissionDeniedError(APIError):
    """403: the key lacks the permission, or the route is not open to keys (`route_not_available`)."""


class NotFoundError(APIError):
    """404: the resource does not exist, or belongs to another workspace than the key's."""


class ConflictError(APIError):
    """409."""


class UnsupportedMediaTypeError(APIError):
    """415: the extension of `file` is not supported and no `file_type` was sent. The body lists
    `supported_file_types`."""


class UnprocessableEntityError(APIError):
    """422: validation (`errors`) or a rule of the send (`window_closed`, `antiblock_*`…)."""


class RateLimitError(APIError):
    """429: a pace (`rate_limited`, `daily_cap_exceeded`; `retry_after` says how many seconds to
    wait), or a limit that waiting does not fix (`mac_lockout_24h`, `too_many_open_links`…)."""


class InternalServerError(APIError):
    """5xx. After a `5xx` on a write, read the state before repeating it: it may have been applied."""


_BY_STATUS = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    415: UnsupportedMediaTypeError,
    422: UnprocessableEntityError,
    429: RateLimitError,
}


class APIConnectionError(FunnelchatError):
    """The request never got a response: DNS, connection refused, reset, TLS…"""

    def __init__(self, message: str = "Could not connect to the Funnelchat API.") -> None:
        super().__init__(message)


class APIConnectionTimeoutError(APIConnectionError):
    """The request took longer than `timeout`."""

    def __init__(self, timeout: float) -> None:
        super().__init__(f"The Funnelchat API did not answer within {timeout:g} s.")


class WebhookVerificationError(FunnelchatError):
    """A webhook delivery did not pass verification. `reason` says which check failed:
    `missing_secret`, `invalid_body`, `missing_header`, `malformed_header`,
    `timestamp_out_of_tolerance`, `signature_mismatch`, `invalid_json` or `invalid_event`."""

    def __init__(self, reason: str, message: str) -> None:
        super().__init__(message)
        self.reason = reason


def request_id_of(headers: Mapping[str, str]) -> Optional[str]:
    """The `X-Request-Id` of a response, or `None` when it has none."""
    value = headers.get("x-request-id")
    return value.strip() if value and value.strip() else None


def parse_retry_after(value: Optional[str], now: Optional[float] = None) -> Optional[float]:
    """Seconds to wait from a `Retry-After` header: delta-seconds (`"30"`) or an HTTP date."""
    if value is None or not value.strip():
        return None
    text = value.strip()
    try:
        seconds = float(text)
    except ValueError:
        pass
    else:
        return seconds if seconds >= 0 else None
    try:
        date = parsedate_to_datetime(text)
    except (TypeError, ValueError, IndexError):
        return None
    if date is None:
        return None
    return max(0.0, float(int(date.timestamp() - (time.time() if now is None else now) + 0.999)))
