class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        result= sorted(nums)

        min1 = result[0]
        min2 = result[1]

        max1=result[-1]
        max2=result[-2]
        max3=result[-3]

        negative_prod= min1*min2*max1
        positive_prod= max1*max2*max3

        maximum_product= max(negative_prod, positive_prod)

        return maximum_product