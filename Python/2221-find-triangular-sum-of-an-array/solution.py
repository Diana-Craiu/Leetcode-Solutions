class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)

        while n>1:
            if n==1:
                break
            else:
                newNums=[]

            for i in range(n-1):
                val=(nums[i]+nums[i+1])%10
                newNums.append(val)
                nums[i]=newNums[i]

            n=n-1

        return nums[0]

        