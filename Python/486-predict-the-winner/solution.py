from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dfs(left, right):
            if left == right:
                return nums[left]

            take_left = nums[left] - dfs(left + 1, right)
            take_right = nums[right] - dfs(left, right - 1)

            return max(take_left, take_right)

        return dfs(0, len(nums) - 1) >= 0