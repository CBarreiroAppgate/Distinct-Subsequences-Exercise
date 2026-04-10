from abc import ABC, abstractmethod


class SubsequenceCounterPort(ABC):
    """Output port for subsequence counting.

    Domain abstraction that decouples the use case from any
    specific counting algorithm implementation.
    """

    @abstractmethod
    def count(self, source: str, target: str) -> int:
        """Return the number of distinct subsequences of target in source."""
