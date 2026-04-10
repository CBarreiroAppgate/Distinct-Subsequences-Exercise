from app.domain.ports.subsequence_counter_port import SubsequenceCounterPort


class SubsequenceCounter(SubsequenceCounterPort):


    def count(self, source: str, target: str) -> int:
        """Return the number of distinct subsequences of target in source.

        Raises:
            ValueError: If source or target is None.
        """
        if source is None or target is None:
            raise ValueError("source and target must not be None")

        if len(target) > len(source):
            return 0

        dp = [1] + [0] * len(target)

        for c in source:
            for j in range(len(target), 0, -1):
                if c == target[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]
