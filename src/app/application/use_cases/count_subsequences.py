from app.application.ports.input.count_subsequences_use_case import CountSubsequencesUseCase
from app.domain.ports.subsequence_counter_port import SubsequenceCounterPort


class CountSubsequences(CountSubsequencesUseCase):

    def __init__(self, counter: SubsequenceCounterPort) -> None:
        self._counter = counter

    def execute(self, source: str, target: str) -> int:
        return self._counter.count(source, target)
