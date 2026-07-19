class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while any(n != 0 for n in nums):
            smallest = [n for n in nums if n != 0]
            if not smallest:
                return 0

            x=min(smallest)

            nums=[n-x if n != 0 else 0 for n in nums]

            count=count+1

        return count


lista= Solution()
numbers = [1,5,0,3,5]
print(lista.minimumOperations(numbers))