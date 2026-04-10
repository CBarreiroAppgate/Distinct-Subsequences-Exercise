import pytest
from unittest.mock import MagicMock
from app.application.use_cases.count_event_subsequences import CountEventSubsequences
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class TestCountEventSubsequencesUseCase:
    def setup_method(self):
        self.counter = MagicMock()
        self.use_case = CountEventSubsequences(self.counter)

    def test_delegates_to_counter_correctly(self):
        query = EventSequenceQuery(
            ["LOGIN", "VIEW", "ADD_TO_CART", "CHECKOUT"],
            ["LOGIN", "ADD_TO_CART", "CHECKOUT"],
        )
        self.counter.count.return_value = 1
        result = self.use_case.execute(query)
        self.counter.count.assert_called_once_with(query)
        assert result == 1

    def test_propagates_value_error_from_domain(self):
        query = EventSequenceQuery(
            ["LOGIN", "VIEW", "ADD_TO_CART", "CHECKOUT"],
            ["LOGIN", "ADD_TO_CART", "CHECKOUT"],
        )
        self.counter.count.side_effect = ValueError("unexpected error")
        with pytest.raises(ValueError, match="unexpected error"):
            self.use_case.execute(query)
