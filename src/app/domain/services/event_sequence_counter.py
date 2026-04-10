from app.application.ports.output.event_sequence_counter_port import EventSequenceCounterPort
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class EventSequenceCounter(EventSequenceCounterPort):

    def count(self, query: EventSequenceQuery) -> int:
        """Return the number of distinct subsequences of query.target in query.source."""
        source, target = query.source, query.target

        if len(target) > len(source):
            return 0

        dp = [1] + [0] * len(target)

        for event in source:
            for j in range(len(target), 0, -1):
                if event == target[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]
