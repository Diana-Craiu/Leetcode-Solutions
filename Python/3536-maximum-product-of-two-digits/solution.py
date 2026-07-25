class Solution:
    def maxProduct(self, n: int) -> int:
        rezultat = "".join(sorted(str(n), reverse=True))
        a = int(rezultat[0])
        b = int(rezultat[1])

        max_product=a*b

        return max_product