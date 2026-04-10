from abc import ABC, abstractmethod

from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class CountEventSubsequencesUseCase(ABC):
    """Input port for the distinct event subsequences use case."""

    @abstractmethod
    def execute(self, query: EventSequenceQuery) -> int:
        """Return the number of distinct subsequences of query.target in query.source.

        Raises:
            ValueError: If query violates problem constraints.
        """
