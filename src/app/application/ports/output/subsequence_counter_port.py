from abc import ABC, abstractmethod
from app.domain.value_objects.subsequence_query import SubsequenceQuery


class SubsequenceCounterPort(ABC):
    @abstractmethod
    def count(self, query: SubsequenceQuery) -> int:
        """Return the number of distinct subsequences of query.target in query.source."""
