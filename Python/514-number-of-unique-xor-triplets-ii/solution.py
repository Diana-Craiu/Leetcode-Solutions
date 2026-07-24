class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        max_xor=2048

        buffer = [[False] * max_xor for _ in range(4)]
        buffer[0][0] = True

        for _ in range(3):
            new = [False] * max_xor

            for x in range(max_xor):
                if not buffer[_][x]:
                    continue

                for num in nums:
                    new[x ^ num] = True

            buffer[_ + 1] = new

        return sum(buffer[3])
