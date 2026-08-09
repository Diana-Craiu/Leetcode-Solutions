from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] =sum from i to the last place
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):
            # if we can take all the remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # try all the possible x
            for X in range(1, 2 * M + 1):
                new_M = max(M, X)

                # the stones we can get
                current = suffix[i] - dp(i + X, new_M)

                best = max(best, current)

            return best

        return dp(0, 1)
        