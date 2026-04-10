from abc import ABC, abstractmethod


class CountSubsequencesUseCase(ABC):
    """Input port for the distinct subsequences use case."""

    @abstractmethod
    def execute(self, source: str, target: str) -> int:
        """Return the number of distinct subsequences of target in source.

        Raises:
            ValueError: If source or target is None.
        """
