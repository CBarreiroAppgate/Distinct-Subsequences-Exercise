import pytest
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class TestEventSequenceQuery:
    def setup_method(self):
        self.valid_source = ["LOGIN", "ADD_ITEM", "checkout-1"]
        self.valid_target = ["LOGIN", "checkout-1"]

    def test_valid_query(self):
        q = EventSequenceQuery(self.valid_source, self.valid_target)
        assert q.source == self.valid_source
        assert q.target == self.valid_target

    def test_raises_on_non_list_source(self):
        with pytest.raises(ValueError, match="source must be a list"):
            EventSequenceQuery("LOGIN ADD_ITEM", self.valid_target)

    def test_raises_on_none_source(self):
        with pytest.raises(ValueError, match="source must be a list"):
            EventSequenceQuery(None, self.valid_target)

    def test_raises_on_empty_source_list(self):
        with pytest.raises(ValueError, match="source length must be between"):
            EventSequenceQuery([], self.valid_target)

    def test_raises_on_source_too_long(self):
        with pytest.raises(ValueError, match="source length must be between"):
            EventSequenceQuery(["event"] * 1001, self.valid_target)

    def test_raises_on_empty_token_in_source(self):
        with pytest.raises(ValueError, match="source token"):
            EventSequenceQuery(["LOGIN", "", "checkout-1"], self.valid_target)

    def test_raises_on_invalid_chars_in_token(self):
        with pytest.raises(ValueError, match="source token"):
            EventSequenceQuery(["ADD TO CART"], self.valid_target)

    def test_equality_same_values(self):
        q1 = EventSequenceQuery(self.valid_source, self.valid_target)
        q2 = EventSequenceQuery(self.valid_source, self.valid_target)
        assert q1 == q2

    def test_equality_different_values(self):
        q1 = EventSequenceQuery(self.valid_source, self.valid_target)
        q2 = EventSequenceQuery(["LOGIN"], self.valid_target)
        assert q1 != q2

    def test_repr(self):
        q = EventSequenceQuery(self.valid_source, self.valid_target)
        assert "LOGIN" in repr(q)