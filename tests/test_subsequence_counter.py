import pytest
from app.domain.services.subsequence_counter import SubsequenceCounter
from app.domain.value_objects.subsequence_query import SubsequenceQuery


class TestSubsequenceCounter:
    def setup_method(self):
        self.counter = SubsequenceCounter()

    def _count(self, source: str, target: str) -> int:
        return self.counter.count(SubsequenceQuery(source, target))

    def test_example_1_rabbbit_rabbit(self):
        assert self._count("rabbbit", "rabbit") == 3

    def test_example_2_babgbag_bag(self):
        assert self._count("babgbag", "bag") == 5

    def test_target_longer_than_source_returns_zero(self):
        assert self._count("ab", "abc") == 0

    def test_identical_strings_returns_one(self):
        assert self._count("abc", "abc") == 1

    def test_single_char_repeated_in_source(self):
        assert self._count("aaa", "a") == 3

    def test_no_common_chars_returns_zero(self):
        assert self._count("abc", "d") == 0

    def test_repeated_pattern(self):
        assert self._count("aabb", "ab") == 4
