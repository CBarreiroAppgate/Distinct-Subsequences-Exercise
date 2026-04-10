from app.domain.services.event_sequence_counter import EventSequenceCounter
from app.application.use_cases.count_event_subsequences import CountEventSubsequences
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class TestEventWiring:
    def setup_method(self):
        counter = EventSequenceCounter()
        self.use_case = CountEventSubsequences(counter)

    def test_login_funnel_end_to_end(self):
        query = EventSequenceQuery(
            ["LOGIN", "VIEW", "ADD_TO_CART", "CHECKOUT"],
            ["LOGIN", "ADD_TO_CART", "CHECKOUT"],
        )
        assert self.use_case.execute(query) == 1

    def test_target_not_found_returns_zero(self):
        query = EventSequenceQuery(
            ["LOGIN", "VIEW"],
            ["CHECKOUT"],
        )
        assert self.use_case.execute(query) == 0
