from math import prod
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        rezultat = prod(int(c) for c in str(n))

        counter= True

        while counter:
            if rezultat % t == 0:
                counter = False
                return n
            else:
                n = n+1
                rezultat = prod(int(c) for c in str(n))