from __future__ import annotations

import re
from typing import List

_MAX_LEN = 1000
_VALID_TOKEN = re.compile(r'^[A-Za-z0-9_\-]+$')


class EventSequenceQuery:
    """Immutable value object representing a validated event-sequence query."""

    def __init__(self, source: List[str], target: List[str]) -> None:
        self._validate("source", source)
        self._validate("target", target)
        self._source = list(source)
        self._target = list(target)

    @staticmethod
    def _validate(name: str, value: object) -> None:
        if not isinstance(value, list):
            raise ValueError(
                f"{name} must be a list, got {type(value).__name__}"
            )
        if len(value) < 1 or len(value) > _MAX_LEN:
            raise ValueError(
                f"{name} length must be between 1 and {_MAX_LEN}, got {len(value)}"
            )
        for token in value:
            if not isinstance(token, str) or len(token) == 0:
                raise ValueError(
                    f"{name} token must be a non-empty string, got {token!r}"
                )
            if not _VALID_TOKEN.match(token):
                raise ValueError(
                    f"{name} token contains invalid characters: {token!r}. "
                    "Only [A-Za-z0-9_-] are allowed."
                )

    @property
    def source(self) -> List[str]:
        return list(self._source)

    @property
    def target(self) -> List[str]:
        return list(self._target)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EventSequenceQuery):
            return NotImplemented
        return self._source == other._source and self._target == other._target

    def __repr__(self) -> str:
        return f"EventSequenceQuery(source={self._source!r}, target={self._target!r})"
