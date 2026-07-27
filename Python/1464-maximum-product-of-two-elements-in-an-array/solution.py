class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=sorted(nums, reverse=True)

        a=result[0]-1
        b=result[1]-1

        maximum=a*b

        return maximum