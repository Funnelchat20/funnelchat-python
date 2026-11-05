"""Pagination over the list routes. Three shapes exist and all are handled:

- page numbers (Laravel): `{"data", "links", "meta": {"current_page", "last_page", …}}`, next with `page`;
- cursors: `{"data", "meta": {"next_cursor", …}}`, next with `cursor`;
- plain lists: one page with everything.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, Generic, Iterator, List, Optional, Tuple, TypeVar
from urllib.parse import parse_qs, urlparse

from ._errors import FunnelchatError

T = TypeVar("T")

#: Fetches one page given its query: returns the decoded body and the `X-Request-Id`.
PageFetcher = Callable[[Dict[str, Any]], Tuple[Any, Optional[str]]]


class Page(Generic[T]):
    """One page of a list. Iterate it to walk every item of this page and the following ones:

        for device in client.devices.list():
            print(device["id"])

    `data` has the items of this page only; `has_next_page()` and `get_next_page()` go page by page.
    """

    def __init__(self, fetch: PageFetcher, query: Dict[str, Any], body: Any, request_id: Optional[str]) -> None:
        self._fetch = fetch
        self._query = query
        #: The items of this page.
        self.data: List[T] = _items(body)
        #: The full response body of this page (with `meta` and `links` when the route sends them).
        self.body: Any = body
        #: The `X-Request-Id` of the response of this page.
        self.request_id: Optional[str] = request_id

    def next_page_query(self) -> Optional[Dict[str, Any]]:
        """The query keys that ask for the next page (`page` or `cursor`), or None on the last page."""
        if not self.data:
            return None
        nxt = next_page_query(self.body)
        if nxt is None:
            return None
        if all(str(self._query.get(k)) == str(v) for k, v in nxt.items()):
            return None
        return nxt

    def has_next_page(self) -> bool:
        return self.next_page_query() is not None

    def get_next_page(self) -> "Page[T]":
        """Fetches the next page. Raises FunnelchatError when there is none: check has_next_page()."""
        nxt = self.next_page_query()
        if nxt is None:
            raise FunnelchatError("There are no more pages.")
        query = {**self._query, **nxt}
        if "cursor" in nxt:
            query.pop("page", None)
        body, request_id = self._fetch(query)
        return Page(self._fetch, query, body, request_id)

    def iter_pages(self) -> Iterator["Page[T]"]:
        """This page and the following ones, page by page."""
        page: Optional[Page[T]] = self
        while page is not None:
            yield page
            page = page.get_next_page() if page.has_next_page() else None

    def __iter__(self) -> Iterator[T]:
        for page in self.iter_pages():
            yield from page.data

    def __repr__(self) -> str:
        return f"<Page of {len(self.data)} items, has_next_page={self.has_next_page()}>"


def _items(body: Any) -> List[Any]:
    if isinstance(body, list):
        return body
    if isinstance(body, dict) and isinstance(body.get("data"), list):
        return list(body["data"])
    return []


def _to_int(value: Any) -> Optional[int]:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def next_page_query(body: Any) -> Optional[Dict[str, Any]]:
    """The query of the next page according to a response body, or None."""
    if not isinstance(body, dict):
        return None
    for holder in (body.get("meta"), body):
        if not isinstance(holder, dict):
            continue
        if "next_cursor" in holder:
            cursor = holder["next_cursor"]
            return {"cursor": cursor} if isinstance(cursor, str) and cursor else None
        current, last = _to_int(holder.get("current_page")), _to_int(holder.get("last_page"))
        if current is not None and last is not None:
            return {"page": current + 1} if current < last else None
    links: Dict[str, Any] = body["links"] if isinstance(body.get("links"), dict) else {}
    next_url = links.get("next") or body.get("next_page_url")
    if isinstance(next_url, str) and next_url:
        params = parse_qs(urlparse(next_url).query)
        if params.get("cursor"):
            return {"cursor": params["cursor"][0]}
        page = _to_int(params["page"][0]) if params.get("page") else None
        if page is not None:
            return {"page": page}
    return None
