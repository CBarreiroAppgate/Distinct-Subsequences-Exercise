from app.application.ports.output.subsequence_counter_port import SubsequenceCounterPort
from app.domain.value_objects.subsequence_query import SubsequenceQuery


class SubsequenceCounter(SubsequenceCounterPort):

    def count(self, query: SubsequenceQuery) -> int:
        """Return the number of distinct subsequences of query.target in query.source."""
        source, target = query.source, query.target

        if len(target) > len(source):
            return 0

        dp = [1] + [0] * len(target)

        for c in source:
            for j in range(len(target), 0, -1):
                if c == target[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]
