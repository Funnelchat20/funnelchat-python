"""The official Python SDK of the Funnelchat API.

    from funnelchat import Funnelchat

    client = Funnelchat()  # reads FUNNELCHAT_API_KEY
    result = client.messages.send_direct(device_id=3, phone="5491100000000", text="Hi Ana!")
    print(result["message"]["id"], result["message"]["status"])  # 1002 queued

The types of the responses and of the webhook events are in `funnelchat.types`.
"""

from . import webhooks
from ._client import BASE_URLS, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, Funnelchat, ResponseInfo
from ._error_codes import (
    ACCESS_ERROR_CODES,
    GROUP_ACTION_ERROR_CODES,
    IDEMPOTENCY_ERROR_CODES,
    NOT_RETRYABLE_CODES,
    NUMBER_ERROR_CODES,
    SEND_ERROR_CODES,
    is_number_quota_error,
    is_send_rule_error,
)
from ._errors import (
    APIConnectionError,
    APIConnectionTimeoutError,
    APIError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    FunnelchatError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
    UnsupportedMediaTypeError,
    WebhookVerificationError,
)
from ._pagination import Page
from ._resource import NOT_GIVEN, NotGiven
from ._routes import ROUTES, WEBHOOK_EVENTS, Route, WebhookEventInfo
from ._version import __version__

__all__ = [
    "Funnelchat",
    "ResponseInfo",
    "BASE_URLS",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "Page",
    "NOT_GIVEN",
    "NotGiven",
    "webhooks",
    "ROUTES",
    "WEBHOOK_EVENTS",
    "Route",
    "WebhookEventInfo",
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
    "ACCESS_ERROR_CODES",
    "SEND_ERROR_CODES",
    "NUMBER_ERROR_CODES",
    "GROUP_ACTION_ERROR_CODES",
    "IDEMPOTENCY_ERROR_CODES",
    "NOT_RETRYABLE_CODES",
    "is_send_rule_error",
    "is_number_quota_error",
    "__version__",
]
