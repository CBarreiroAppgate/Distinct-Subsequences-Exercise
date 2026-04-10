from typing import List

from app.domain.services.event_sequence_counter import EventSequenceCounter
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class TestEventSequenceCounter:
    def setup_method(self):
        self.counter = EventSequenceCounter()

    def _count(self, source: List[str], target: List[str]) -> int:
        return self.counter.count(EventSequenceQuery(source, target))

    def test_login_funnel(self):
        source = ["LOGIN", "VIEW", "ADD_TO_CART", "CHECKOUT"]
        target = ["LOGIN", "ADD_TO_CART", "CHECKOUT"]
        assert self._count(source, target) == 1

    def test_multiple_occurrences(self):
        source = ["A", "B", "A", "B", "C"]
        target = ["A", "B", "C"]
        assert self._count(source, target) == 3

    def test_target_longer_than_source_returns_zero(self):
        source = ["A"]
        target = ["A", "B"]
        assert self._count(source, target) == 0

    def test_identical_sequences_returns_one(self):
        source = ["LOGIN", "ADD_TO_CART", "CHECKOUT"]
        target = ["LOGIN", "ADD_TO_CART", "CHECKOUT"]
        assert self._count(source, target) == 1

    def test_no_matching_events_returns_zero(self):
        source = ["LOGIN", "VIEW"]
        target = ["CHECKOUT"]
        assert self._count(source, target) == 0
