"""The client of the Funnelchat public API."""

from __future__ import annotations

import json
import os
import platform
import time
from typing import Any, Callable, Dict, Mapping, Optional, Tuple

import httpx

from ._error_codes import NOT_RETRYABLE_CODES
from ._errors import APIConnectionError, APIConnectionTimeoutError, APIError, FunnelchatError, request_id_of
from ._pagination import Page
from ._query import interpolate_path, serialize_query
from ._retry import is_retryable, is_send_request, retry_delay
from ._version import __version__
from .resources import ClientResources

__all__ = ["Funnelchat", "ResponseInfo", "BASE_URLS", "DEFAULT_TIMEOUT", "DEFAULT_MAX_RETRIES"]

#: The base URL of each environment: one URL for the whole public API.
BASE_URLS: Dict[str, str] = {
    "production": "https://api.funnelchat.com",
    "staging": "https://api-staging.funnelchat.com",
}
#: Maximum seconds of each attempt.
DEFAULT_TIMEOUT = 30.0
#: Automatic retries (see the README, Retries).
DEFAULT_MAX_RETRIES = 2


class ResponseInfo:
    """What the API answered to one request, besides the body: `status`, `request_id` (the
    `X-Request-Id`, quote it when you report a problem), `headers`, `method` and `url`."""

    def __init__(self, status: int, headers: httpx.Headers, method: str, url: str) -> None:
        self.status = status
        self.headers = headers
        self.method = method
        self.url = url
        self.request_id = request_id_of(headers)

    def __repr__(self) -> str:
        return f"<ResponseInfo {self.method} {self.url} {self.status} request_id={self.request_id}>"


class Funnelchat(ClientResources):
    """Client of the Funnelchat public API.

        from funnelchat import Funnelchat

        client = Funnelchat()  # reads FUNNELCHAT_API_KEY
        for device in client.devices.list():
            print(device["id"], device["alias"])

    Responses are plain dicts (the decoded JSON), typed with the TypedDicts of `funnelchat.types`.
    The key never shows up in `repr(client)` or in an error.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        environment: str = "production",
        base_url: Optional[str] = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Optional[Mapping[str, str]] = None,
        http_client: Optional[httpx.Client] = None,
    ) -> None:
        """
        - `api_key`: `<id>|fc_live_...`. Default: the `FUNNELCHAT_API_KEY` environment variable.
        - `environment`: `production` (`https://api.funnelchat.com`) or `staging`.
        - `base_url`: another base URL (for example the sandbox's); it wins over `environment`.
        - `timeout`: maximum seconds of each attempt. Default 30.
        - `max_retries`: automatic retries on `429`, `5xx` and network errors. Default 2; 0 turns them off.
        - `default_headers`: headers sent with every request.
        - `http_client`: your own `httpx.Client` (proxies, transports…). You close it.
        """
        key = api_key if api_key is not None else os.environ.get("FUNNELCHAT_API_KEY", "")
        key = key.strip()
        if not key:
            raise FunnelchatError(
                "Missing API key: pass it as `api_key` or in the FUNNELCHAT_API_KEY environment variable."
            )
        if environment not in BASE_URLS:
            raise FunnelchatError(f'Unknown environment: {environment!r}. Use "production" or "staging".')
        self._api_key = key
        self.base_url = (base_url or BASE_URLS[environment]).rstrip("/")
        self.timeout = float(timeout)
        self.max_retries = int(max_retries)
        self._default_headers = dict(default_headers or {})
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else httpx.Client()
        self._sleep: Callable[[float], None] = time.sleep
        #: The status, headers and `X-Request-Id` of the last response this client got.
        self.last_response: Optional[ResponseInfo] = None
        self._init_resources()

    def __repr__(self) -> str:
        return f"Funnelchat(base_url={self.base_url!r}, timeout={self.timeout:g}, max_retries={self.max_retries})"

    def close(self) -> None:
        """Closes the HTTP connections (only those of the httpx.Client the SDK built)."""
        if self._owns_http:
            self._http.close()

    def __enter__(self) -> "Funnelchat":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # -- any route ------------------------------------------------------------------------------

    def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
        idempotency_key: Optional[str] = None,
    ) -> Any:
        """Calls any route and returns the decoded body (None for an empty answer).

            contact = client.request("GET", "/api/v1/contacts/{contact}", path_params={"contact": 2001})
        """
        body_out, _ = self._send(
            method,
            path,
            path_params=path_params,
            query=query,
            body=body,
            headers=headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
            idempotency_key=idempotency_key,
        )
        return body_out

    def paginate(
        self,
        path: str,
        *,
        path_params: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[Any]:
        """Fetches the first page of any list route; iterate it for every item of every page."""
        first_query = dict(query or {})

        def fetch(page_query: Dict[str, Any]) -> Tuple[Any, Optional[str]]:
            return self._send(
                "GET",
                path,
                path_params=path_params,
                query=page_query,
                headers=headers,
                timeout=timeout,
                max_retries=max_retries,
            )

        body, request_id = fetch(first_query)
        return Page(fetch, first_query, body, request_id)

    # -- transport --------------------------------------------------------------------------------

    def _send(
        self,
        method: str,
        template: str,
        *,
        path_params: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
        idempotency_key: Optional[str] = None,
    ) -> Tuple[Any, Optional[str]]:
        verb = method.upper()
        pathname = interpolate_path(template, path_params)
        url = self.base_url + (pathname if pathname.startswith("/") else f"/{pathname}")
        attempts = max(0, self.max_retries if max_retries is None else int(max_retries))
        attempt_timeout = self.timeout if timeout is None else float(timeout)
        is_send = is_send_request(verb, pathname.split("?")[0])
        # A send is never repeated unless the caller asks; then it follows the rule of every write.
        retries_allowed = retry_send or not is_send
        # With an idempotency key the API answers the same resource to a repeated create, so it is
        # retried like a PUT (as in funnelchat-php). A send is not, key or no key.
        retry_as = "PUT" if idempotency_key is not None and not is_send else verb

        request_headers: Dict[str, str] = {
            "Accept": "application/json",
            "User-Agent": f"funnelchat-python/{__version__} python/{platform.python_version()}",
        }
        content: Optional[bytes] = None
        if body is not None:
            content = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
            request_headers["Content-Type"] = "application/json"
        request_headers.update(self._default_headers)
        request_headers.update(headers or {})
        if idempotency_key is not None:
            if not 1 <= len(idempotency_key) <= 255:
                raise FunnelchatError("`idempotency_key` must have between 1 and 255 characters.")
            request_headers["Idempotency-Key"] = idempotency_key
        request_headers["Authorization"] = f"Bearer {self._api_key}"
        params = tuple(serialize_query(query))

        attempt = 0
        while True:
            can_retry = retries_allowed and attempt < attempts
            try:
                response = self._http.request(
                    verb, url, params=params, content=content, headers=request_headers, timeout=attempt_timeout
                )
            except httpx.TimeoutException:
                failure: APIConnectionError = APIConnectionTimeoutError(attempt_timeout)
            except httpx.RequestError as error:
                failure = APIConnectionError(f"Could not connect to the Funnelchat API: {type(error).__name__}.")
            else:
                self.last_response = ResponseInfo(response.status_code, response.headers, verb, url)
                decoded = _decode(response)
                if response.is_success:
                    return decoded, self.last_response.request_id
                api_error = APIError.from_response(
                    status=response.status_code, body=decoded, headers=response.headers, method=verb, url=url
                )
                if can_retry and is_retryable(retry_as, response.status_code) and api_error.code not in NOT_RETRYABLE_CODES:
                    delay = retry_delay(attempt, api_error.retry_after)
                    if delay is not None:
                        self._sleep(delay)
                        attempt += 1
                        continue
                raise api_error
            if can_retry and is_retryable(retry_as, None):
                self._sleep(retry_delay(attempt, None) or 0.0)
                attempt += 1
                continue
            raise failure


def _decode(response: httpx.Response) -> Any:
    """The body: JSON when it parses, the text otherwise, None when there is none (a `204`)."""
    text = response.text
    if text == "":
        return None
    content_type = response.headers.get("content-type", "")
    if "json" in content_type or text.lstrip()[:1] in ("{", "["):
        try:
            return json.loads(text)
        except ValueError:
            return text
    return text
