from abc import ABC, abstractmethod

from app.domain.value_objects.subsequence_query import SubsequenceQuery


class CountSubsequencesUseCase(ABC):
    """Input port for the distinct subsequences use case."""

    @abstractmethod
    def execute(self, query: SubsequenceQuery) -> int:
        """Return the number of distinct subsequences of query.target in query.source.

        Raises:
            ValueError: If query violates problem constraints.
        """
