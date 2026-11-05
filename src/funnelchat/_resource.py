"""The base of every resource and the marker of an argument that was not given."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Mapping, Optional

if TYPE_CHECKING:
    from ._client import Funnelchat
    from ._pagination import Page


class NotGiven:
    """The default of the optional arguments: the field is left out of the request. `None` is sent
    as JSON `null` (for example to clear a field)."""

    _instance: Optional["NotGiven"] = None

    def __new__(cls) -> "NotGiven":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()


def _given(values: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    return {k: v for k, v in (values or {}).items() if v is not NOT_GIVEN}


class Resource:
    """A group of operations of one piece of the API, bound to a client."""

    def __init__(self, client: "Funnelchat") -> None:
        self._client = client

    def __repr__(self) -> str:
        return f"<{type(self).__name__} resource>"

    def _request(
        self,
        method: str,
        path: str,
        *,
        path_params: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_body: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
        idempotency_key: Optional[str] = None,
    ) -> Any:
        if isinstance(body, Mapping) or extra_body:
            body = {**_given(body if isinstance(body, Mapping) else None), **(extra_body or {})}
        return self._client.request(
            method,
            path,
            path_params=path_params,
            query={**_given(query), **(extra_query or {})} or None,
            body=body,
            headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
            idempotency_key=idempotency_key,
        )

    def _paginate(
        self,
        path: str,
        *,
        path_params: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        extra_query: Optional[Mapping[str, Any]] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> "Page[Any]":
        return self._client.paginate(
            path,
            path_params=path_params,
            query={**_given(query), **(extra_query or {})},
            headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )
