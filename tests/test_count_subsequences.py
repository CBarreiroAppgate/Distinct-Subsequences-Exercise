import pytest
from unittest.mock import MagicMock
from app.application.use_cases.count_subsequences import CountSubsequences
from app.domain.value_objects.subsequence_query import SubsequenceQuery


class TestCountSubsequencesUseCase:
    def setup_method(self):
        self.counter = MagicMock()
        self.use_case = CountSubsequences(self.counter)

    def test_delegates_to_counter_correctly(self):
        query = SubsequenceQuery("rabbbit", "rabbit")
        self.counter.count.return_value = 3
        result = self.use_case.execute(query)
        self.counter.count.assert_called_once_with(query)
        assert result == 3

    def test_propagates_value_error_from_domain(self):
        query = SubsequenceQuery("rabbbit", "rabbit")
        self.counter.count.side_effect = ValueError("unexpected error")
        with pytest.raises(ValueError, match="unexpected error"):
            self.use_case.execute(query)
