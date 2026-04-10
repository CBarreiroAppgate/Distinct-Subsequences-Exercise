from abc import ABC, abstractmethod
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class EventSequenceCounterPort(ABC):
    @abstractmethod
    def count(self, query: EventSequenceQuery) -> int:
        """Return the number of distinct subsequences of query.target in query.source."""
