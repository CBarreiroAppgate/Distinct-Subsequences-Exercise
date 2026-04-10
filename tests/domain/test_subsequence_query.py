import pytest
from app.domain.value_objects.subsequence_query import SubsequenceQuery


class TestSubsequenceQuery:
    def test_valid_query(self):
        q = SubsequenceQuery("rabbbit", "rabbit")
        assert q.source == "rabbbit"
        assert q.target == "rabbit"

    def test_raises_on_none_source(self):
        with pytest.raises(ValueError, match="source must be a string"):
            SubsequenceQuery(None, "rabbit")

    def test_raises_on_none_target(self):
        with pytest.raises(ValueError, match="target must be a string"):
            SubsequenceQuery("rabbbit", None)

    def test_raises_on_empty_source(self):
        with pytest.raises(ValueError, match="source"):
            SubsequenceQuery("", "rabbit")

    def test_raises_on_empty_target(self):
        with pytest.raises(ValueError, match="target"):
            SubsequenceQuery("rabbbit", "")

    def test_raises_on_source_too_long(self):
        with pytest.raises(ValueError, match="source"):
            SubsequenceQuery("a" * 1001, "a")

    def test_raises_on_target_too_long(self):
        with pytest.raises(ValueError, match="target"):
            SubsequenceQuery("a", "a" * 1001)

    def test_raises_on_non_english_chars_source(self):
        with pytest.raises(ValueError, match="source"):
            SubsequenceQuery("abc123", "abc")

    def test_raises_on_non_english_chars_target(self):
        with pytest.raises(ValueError, match="target"):
            SubsequenceQuery("abc", "a1")

    def test_equality_same_values(self):
        assert SubsequenceQuery("abc", "ab") == SubsequenceQuery("abc", "ab")

    def test_equality_different_values(self):
        assert SubsequenceQuery("abc", "ab") != SubsequenceQuery("abc", "ac")

    def test_repr(self):
        q = SubsequenceQuery("abc", "ab")
        assert "abc" in repr(q)
        assert "ab" in repr(q)
