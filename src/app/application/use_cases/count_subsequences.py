from app.application.ports.input.count_subsequences_use_case import CountSubsequencesUseCase
from app.application.ports.output.subsequence_counter_port import SubsequenceCounterPort
from app.domain.value_objects.subsequence_query import SubsequenceQuery


class CountSubsequences(CountSubsequencesUseCase):

    def __init__(self, counter: SubsequenceCounterPort) -> None:
        self._counter = counter

    def execute(self, query: SubsequenceQuery) -> int:
        return self._counter.count(query)
