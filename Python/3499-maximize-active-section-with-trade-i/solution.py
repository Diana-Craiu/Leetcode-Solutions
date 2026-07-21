class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count("1")

        max_gain = 0
        left_zero_block = -float("inf")

        i = 0

        while i < len(s):
            j = i

            # gasim blocul curent
            while j < len(s) and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == "0":
                # daca exista un bloc de 0 inainte, putem verifica cat caștigam daca eliminam blocul de 1 dintre ele
                max_gain = max(max_gain, left_zero_block + length)

                # acesta devine ultimul bloc de 0 intalnit
                left_zero_block = length

            i = j

        return total_ones + max_gain