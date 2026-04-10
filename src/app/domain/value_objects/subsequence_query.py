import re

_MAX_LEN = 1000
_VALID = re.compile(r'^[a-zA-Z]+$')


class SubsequenceQuery:
    """Immutable value object representing a validated subsequence query."""

    def __init__(self, source: str, target: str) -> None:
        self._validate("source", source)
        self._validate("target", target)
        self._source = source
        self._target = target

    @staticmethod
    def _validate(name: str, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"{name} must be a string, got {type(value).__name__}")
        if len(value) < 1 or len(value) > _MAX_LEN:
            raise ValueError(f"{name} length must be between 1 and {_MAX_LEN}, got {len(value)}")
        if not _VALID.match(value):
            raise ValueError(f"{name} must contain only English letters")

    @property
    def source(self) -> str:
        return self._source

    @property
    def target(self) -> str:
        return self._target

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SubsequenceQuery):
            return NotImplemented
        return self._source == other._source and self._target == other._target

    def __repr__(self) -> str:
        return f"SubsequenceQuery(source={self._source!r}, target={self._target!r})"
