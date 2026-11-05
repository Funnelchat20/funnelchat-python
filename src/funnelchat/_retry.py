"""The retry policy: which failures are retried, how long to wait, and which requests are sends."""

from __future__ import annotations

import random
import re
from typing import Callable, List, Optional, Pattern

from ._routes import ROUTES

#: First backoff delay, in seconds; it doubles on every retry.
INITIAL_RETRY_DELAY = 0.5
#: Ceiling of the exponential backoff, in seconds.
MAX_RETRY_DELAY = 8.0
#: A `Retry-After` longer than this is not waited for: the error is raised right away with its
#: `retry_after`, so the caller decides (a daily cap can ask for hours).
MAX_RETRY_AFTER_SECONDS = 60.0

_IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})


def is_retryable(method: str, status: Optional[int]) -> bool:
    """Whether a failed attempt may be repeated automatically (`status` None: no response arrived).

    - `GET`, `PUT` and `DELETE`: on `429`, `5xx` and network errors (timeouts included).
    - `POST` and `PATCH` (writes): only when the call was certainly not applied, `429` and `503`. A
      `500`, `502` or `504`, a timeout or a dropped connection can come after the write was applied,
      so the error is raised: read the state before repeating the write.
    """
    if method.upper() in _IDEMPOTENT_METHODS:
        return status is None or status == 429 or status >= 500
    return status in (429, 503)


def retry_delay(attempt: int, retry_after: Optional[float], rand: Callable[[], float] = random.random) -> Optional[float]:
    """Seconds to wait before retry number `attempt` (0 = first retry), or None when the server
    asked for a wait longer than MAX_RETRY_AFTER_SECONDS. With `Retry-After` the wait is exactly
    what it asks for; without it, exponential backoff with up to 25 % of jitter."""
    if retry_after is not None:
        return None if retry_after > MAX_RETRY_AFTER_SECONDS else max(0.0, retry_after)
    base = min(INITIAL_RETRY_DELAY * (2.0 ** min(attempt, 30)), MAX_RETRY_DELAY)
    return base * (1 - 0.25 * rand())


def _send_patterns() -> List[Pattern[str]]:
    patterns = []
    for route in ROUTES:
        if route.method == "POST" and (route.permission or "").endswith(":send"):
            parts = re.split(r"\{[^}]+\}", route.path)
            patterns.append(re.compile("^" + "[^/]+".join(re.escape(p) for p in parts) + "/?$"))
    return patterns


#: The send operations of the spec (a `POST` that needs a **Send** permission): they deliver a
#: WhatsApp message and are not idempotent, so they are never retried automatically. Built from
#: the generated route table, so a regeneration keeps the list current.
_SEND_PATTERNS = _send_patterns()


def is_send_request(method: str, pathname: str) -> bool:
    """Whether `method` + `pathname` (already interpolated, without query) is a send."""
    return method.upper() == "POST" and any(p.match(pathname) for p in _SEND_PATTERNS)
