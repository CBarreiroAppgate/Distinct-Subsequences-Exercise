import pytest
from app.domain.services.subsequence_counter import SubsequenceCounter


class TestSubsequenceCounter:
    def setup_method(self):
        self.counter = SubsequenceCounter()

    def test_example_1_rabbbit_rabbit(self):
        assert self.counter.count("rabbbit", "rabbit") == 3

    def test_example_2_babgbag_bag(self):
        assert self.counter.count("babgbag", "bag") == 5

    def test_target_longer_than_source_returns_zero(self):
        assert self.counter.count("ab", "abc") == 0

    def test_empty_target_returns_one(self):
        assert self.counter.count("abc", "") == 1

    def test_empty_source_and_target_returns_one(self):
        assert self.counter.count("", "") == 1

    def test_empty_source_nonempty_target_returns_zero(self):
        assert self.counter.count("", "a") == 0

    def test_identical_strings_returns_one(self):
        assert self.counter.count("abc", "abc") == 1

    def test_single_char_repeated_in_source(self):
        assert self.counter.count("aaa", "a") == 3

    def test_no_common_chars_returns_zero(self):
        assert self.counter.count("abc", "d") == 0

    def test_repeated_pattern(self):
        assert self.counter.count("aabb", "ab") == 4

    def test_raises_on_none_source(self):
        with pytest.raises(ValueError):
            self.counter.count(None, "rabbit")

    def test_raises_on_none_target(self):
        with pytest.raises(ValueError):
            self.counter.count("rabbbit", None)

    def test_raises_on_both_none(self):
        with pytest.raises(ValueError):
            self.counter.count(None, None)
