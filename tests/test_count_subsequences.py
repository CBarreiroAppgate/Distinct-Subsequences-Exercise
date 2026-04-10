from app.application.use_cases.count_subsequences import CountSubsequences
from app.domain.services.subsequence_counter import SubsequenceCounter
import pytest


class TestCountSubsequencesUseCase:
    def setup_method(self):
        counter = SubsequenceCounter()
        self.use_case = CountSubsequences(counter)

    def test_delegates_to_counter_correctly(self):
        assert self.use_case.execute("rabbbit", "rabbit") == 3

    def test_raises_on_none_source(self):
        with pytest.raises(ValueError):
            self.use_case.execute(None, "rabbit")

    def test_raises_on_none_target(self):
        with pytest.raises(ValueError):
            self.use_case.execute("rabbbit", None)

    def test_raises_on_both_none(self):
        with pytest.raises(ValueError):
            self.use_case.execute(None, None)

    def test_empty_strings_valid_input(self):
        assert self.use_case.execute("", "") == 1