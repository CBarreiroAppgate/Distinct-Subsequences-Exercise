import pytest
from unittest.mock import MagicMock
from app.application.use_cases.count_subsequences import CountSubsequences


class TestCountSubsequencesUseCase:
    def setup_method(self):
        self.counter = MagicMock()
        self.use_case = CountSubsequences(self.counter)

    def test_delegates_to_counter_correctly(self):
        self.counter.count.return_value = 3
        result = self.use_case.execute("rabbbit", "rabbit")
        self.counter.count.assert_called_once_with("rabbbit", "rabbit")
        assert result == 3

    def test_propagates_value_error_from_domain(self):
        self.counter.count.side_effect = ValueError("source and target must not be None")
        with pytest.raises(ValueError, match="must not be None"):
            self.use_case.execute(None, "rabbit")
