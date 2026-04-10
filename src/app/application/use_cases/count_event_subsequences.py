from app.application.ports.input.count_event_subsequences_use_case import CountEventSubsequencesUseCase
from app.application.ports.output.event_sequence_counter_port import EventSequenceCounterPort
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class CountEventSubsequences(CountEventSubsequencesUseCase):

    def __init__(self, counter: EventSequenceCounterPort) -> None:
        self._counter = counter

    def execute(self, query: EventSequenceQuery) -> int:
        return self._counter.count(query)
