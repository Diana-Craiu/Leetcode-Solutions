from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #the number of piles is always odd so Alice can always win, so we can return true and that's it.... it's not a good approach for an interview tho...
        # return True

        n = len(piles)

        @cache
        def dp(left, right):
            # only one pile left
            if left == right:
                return piles[left]

            # choose left
            take_left = piles[left] - dp(left + 1, right)

            # choose right
            take_right = piles[right] - dp(left, right - 1)

            return max(take_left, take_right)

        return dp(0, n - 1) > 0