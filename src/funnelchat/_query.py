"""Paths and query strings, the way the API (Laravel) reads them."""

from __future__ import annotations

import re
from datetime import date, datetime
from typing import Any, List, Mapping, Optional, Tuple
from urllib.parse import quote


def serialize_query(query: Optional[Mapping[str, Any]]) -> List[Tuple[str, str]]:
    """The query as `(key, value)` pairs:

    - lists as `key[]=a&key[]=b` (a key already written as `key[]` is not doubled);
    - lists of dicts and nested dicts with brackets: `filters[0][mode]=all`;
    - booleans as `1` / `0` (Laravel's `boolean` rule rejects `true` / `false`);
    - dates as ISO 8601;
    - `None` is left out.
    """
    pairs: List[Tuple[str, str]] = []
    for key, value in (query or {}).items():
        _append(pairs, key, value)
    return pairs


def _append(pairs: List[Tuple[str, str]], key: str, value: Any) -> None:
    if value is None:
        return
    if isinstance(value, (list, tuple)):
        scalar_key = key if key.endswith("[]") else f"{key}[]"
        base = key[:-2] if key.endswith("[]") else key
        for index, item in enumerate(value):
            if isinstance(item, (dict, list, tuple)):
                _append(pairs, f"{base}[{index}]", item)
            else:
                _append(pairs, scalar_key, item)
        return
    if isinstance(value, Mapping):
        for child, child_value in value.items():
            _append(pairs, f"{key}[{child}]", child_value)
        return
    if isinstance(value, bool):
        pairs.append((key, "1" if value else "0"))
        return
    if isinstance(value, (datetime, date)):
        pairs.append((key, value.isoformat()))
        return
    pairs.append((key, str(value)))


def interpolate_path(template: str, params: Optional[Mapping[str, Any]]) -> str:
    """Replaces the `{name}` placeholders of a path with URL-encoded values. Raises ValueError when a
    placeholder has no value, so a request never goes out with `{contact}` in it."""

    def replace(match: "re.Match[str]") -> str:
        name = match.group(1)
        value = (params or {}).get(name)
        if value is None or value == "":
            raise ValueError(f'Missing path parameter "{name}" for {template}.')
        return quote(str(value), safe="")

    return re.sub(r"\{([^}]+)\}", replace, template)
