"""The stable `error` codes of the API (`APIError.code`), with their HTTP status.

Decide by `status` and `code`, never by `message`: its text and language change by area. The same
tables as funnelchat-node 0.4.0 (src/core/error-codes.ts). Sources, all in production on
04-11-2026: the key gate as accounts v1.5.97 runs it; the API entry as deployed to production on
25-10-2026; conversations v1.19.7 (the send rules and the checks before sending a form); accounts
v1.5.97 (creating and connecting numbers); communities v2.35.5 and v2.35.7 (the rejections of a
group action). The spec the portal publishes (portal v0.6.15) declares the common codes every area
answers with, those of the key gate in its `403` and `429`, and many of the rest in the operations
that answer them, but not those of the API entry. When it declares all of them, these tables can be
generated.
"""

from __future__ import annotations

from typing import Dict, FrozenSet, Optional

__all__ = [
    "ACCESS_ERROR_CODES",
    "SEND_ERROR_CODES",
    "NUMBER_ERROR_CODES",
    "GROUP_ACTION_ERROR_CODES",
    "IDEMPOTENCY_ERROR_CODES",
    "TEMPLATE_SYNC_ERROR_CODES",
    "NOT_RETRYABLE_CODES",
    "is_send_rule_error",
    "is_number_quota_error",
]

#: Errors any route can answer: those of the API entry and of the key gate, and the common ones
#: every area answers with, as the spec the portal publishes (portal v0.6.15) declares them.
ACCESS_ERROR_CODES: Dict[str, int] = {
    "unauthenticated": 401,  # missing or invalid API key
    "payment_required": 402,  # the account's payment is overdue: pay it in the Funnelchat panel
    "not_found": 404,  # does not exist, or belongs to another account or workspace: both answer the same
    "conflict": 409,  # the current state does not allow it (the common code of a 409)
    "validation_failed": 422,  # the request is not valid; `errors` says which fields
    "rate_limited": 429,  # with Retry-After: the per-minute limit of the route (the spec gives each one)
    "bad_request": 400,  # the request could not be read (the common code of a 400)
    "forbidden": 403,  # the caller cannot use this route (the common code of a 403)
    "permission_denied": 403,  # the key lacks the permission the route needs (`message` names it)
    "route_not_available": 403,  # the route is not open to API keys (or is turned off)
    "workspace_deleted": 403,  # the key's workspace no longer exists
    "workspace_permission_denied": 403,  # the key's user lacks that permission in its workspace (its role)
    "workspace_foreign_account": 403,  # only a key of a workspace of the account itself can use the route
    "workspace_account_level": 403,  # the route is about the whole account: only a key of the default workspace
    "route_not_found": 404,  # the path does not exist in the public API
    "daily_cap_exceeded": 429,  # with Retry-After: the daily call cap of the key in that area
    "internal_error": 500,  # (502 on some routes) report it with the request id; after a write, read the state
    "edge_misconfigured": 500,  # our problem: report it with the request id
    "origin_unreachable": 502,  # no guarantee the area did not get the call: read the state after a write
    "gate_unavailable": 503,  # with Retry-After: nothing ran; safe to retry
}

#: Rejections of a send with an API key: nothing was sent and nothing was stored.
SEND_ERROR_CODES: Dict[str, int] = {
    "rate_limited": 429,  # with Retry-After: the number's pace
    "mac_lockout_24h": 429,  # 24-hour lockout after using up the monthly active contacts; not worth retrying
    "mac_limit_reached": 429,  # the monthly active contacts are used up; not worth retrying
    "window_closed": 422,  # free text outside the 24-hour window on an official number: send a template
    "antiblock_duplicate_content": 422,  # the same content again to a contact that did not answer
    "antiblock_unanswered_limit": 422,  # too many messages in a row to a contact that did not answer
    "recipient_mismatch": 422,  # the `phone` / `whatsapp_id` is not the contact of the route
    "recipient_unsupported": 422,  # the contact is a group, a broadcast list or a channel
    "provider_unsupported": 422,  # the number cannot send this (see its `capabilities`)
    "device_unavailable": 422,  # the number is not connected or cannot send now
    "not_sent": 422,  # the message could not be registered for sending
    "recipient_unreachable": 422,  # the contact cannot be reached on WhatsApp (forms)
    "contact_blocked": 422,  # the contact is blocked on that number (forms)
    "template_unresolved_placeholder": 422,  # a template variable points to a field that does not exist
    "template_not_found": 404,  # the template is not one this account can send
    "form_not_found": 404,  # the form does not exist
    "form_not_published": 422,  # the form is not published
    "form_not_on_number": 422,  # the form is not published on that number
    "number_not_eligible": 422,  # the number cannot send forms
}

#: Rejections of creating a number, asking for its QR or creating, reading or revoking a connect
#: link: nothing was created. A code with two statuses has the one of the create here.
NUMBER_ERROR_CODES: Dict[str, int] = {
    "numbers_not_included": 403,  # the plan does not include numbers
    "number_limit_reached": 403,  # every number of the plan is in use (`limit`, `used`, `pending_device_ids`)
    "connect_not_allowed": 403,  # the account cannot connect numbers now
    "payment_required": 402,  # the account's payment is overdue (also in ACCESS_ERROR_CODES)
    "pending_number_exists": 409,  # a QR number is already waiting to be scanned; the body brings its `device_id`
    "qr_requires_coexistence": 422,  # (409 on `devices.qr()`) QR only on an official number in coexistence
    "method_already_present": 422,  # the number already has that method; the body brings its `device_id`
    "invalid_reference_device": 422,  # `same_number_as` or `device_id` is not a number that can take it
    "connection_type_mismatch": 422,  # a link with `device_id` of a number that connects another way
    "number_suspended_by_plan": 422,  # (409 on `devices.qr()`) suspended: the plan has fewer numbers
    "invalid_request": 422,  # the body is not valid; `errors` says which fields
    "trial_number_blocked": 409,  # `devices.qr()` of a trial number that is blocked
    "device_inactive": 409,  # `devices.qr()` of a number that is turned off
    "provisioning_quota_exceeded": 409,  # `devices.qr()` when no more QR sessions can start now
    "link_not_pending": 409,  # revoking a connect link that already ended
    "too_many_open_links": 429,  # 20 connect links open: revoke some; not worth retrying
    "provider_error": 500,  # (502 on `devices.qr()` and `devices.status()`) the WhatsApp provider failed
    "meta_connect_disabled": 503,  # official numbers cannot be connected by link yet; QR links work
    "credentials_not_allowed": 403,  # the connect page was opened with a key or a session
}

#: Rejections of a message to a group, of following a group and of reading a group action: nothing
#: was queued or imported. A number or group of another workspace is answered as missing.
GROUP_ACTION_ERROR_CODES: Dict[str, int] = {
    "device_not_found": 404,  # `device_id` is not a number of the key's workspace
    "group_not_found": 404,  # the group is not one of the key's workspace
    "action_not_found": 404,  # `groups.retrieve_action()` of an action that does not exist
    "unsupported_group_type": 422,  # the uid is a community or a channel, not a group
    "device_not_connected": 422,  # the number is not connected
    "device_not_group_admin": 422,  # a QR number that is not admin of the group
    "device_not_group_number": 422,  # an official group that belongs to another number
    "provider_unsupported": 422,  # the number cannot do it (`provider`, maybe `requires`, in the body)
    "window_closed": 422,  # an official number outside the 24-hour window of the group
    "number_restricted": 422,  # Meta restricted the official number
    "unsupported_type": 422,  # that `type` cannot be sent to this group by this number
    "too_many_pending_actions": 429,  # 50 group actions open on the number; not worth retrying
    "import_permission_required": 403,  # following a group needs Groups and campaigns → Manage groups
    "import_rate_limited": 429,  # with Retry-After: the number already followed 5 groups this minute
    "import_in_progress": 409,  # another call is following the same group right now
}

#: Rejections of a create sent with `idempotency_key`.
IDEMPOTENCY_ERROR_CODES: Dict[str, int] = {
    "idempotency_key_mismatch": 422,  # the key was already used with another body
    "invalid_idempotency_key": 422,  # the key is not 1 to 255 characters
    "operation_in_progress": 409,  # the first call with that key is still running
}

#: Rejections of bringing a number's templates from Meta (`templates.sync()`), as the spec the portal
#: publishes (portal v0.6.15) enumerates them for `POST /api/v1/devices/{device}/templates`. A number
#: that does not exist, or is of another workspace, is a `404 not_found`.
TEMPLATE_SYNC_ERROR_CODES: Dict[str, int] = {
    "template_sync_in_progress": 409,  # one is already running for that number: do not start another
    "number_not_connected_to_meta": 422,  # a QR number, or one without a WhatsApp Business account or credentials
    "meta_rejected": 422,  # Meta refused and nothing was brought; its code in `meta_code`
    "meta_unavailable": 502,  # Meta did not answer
}

#: Codes a retry would only repeat: never retried automatically.
NOT_RETRYABLE_CODES: FrozenSet[str] = frozenset(
    {"mac_lockout_24h", "mac_limit_reached", "too_many_open_links", "too_many_pending_actions", "meta_connect_disabled"}
)

_QUOTA_CODES = frozenset(
    {"numbers_not_included", "number_limit_reached", "pending_number_exists", "qr_requires_coexistence", "method_already_present"}
)


def is_send_rule_error(code: Optional[str]) -> bool:
    """Whether an `APIError.code` is a rejection of a send: nothing was sent and nothing was stored."""
    return code is not None and code in SEND_ERROR_CODES


def is_number_quota_error(code: Optional[str]) -> bool:
    """Whether an `APIError.code` is a rejection by the number quota of the plan (the same as the panel's)."""
    return code is not None and code in _QUOTA_CODES
