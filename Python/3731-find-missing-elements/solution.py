class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sorted_nums= sorted(nums)

        first = sorted_nums[0]
        last=sorted_nums[-1]

        full_range = list(range(first, last+1))

        missing_int = sorted(list(set(nums) ^ set(full_range)))

        return missing_int