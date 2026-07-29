from collections import Counter

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:

        freq = Counter(s)

        middle = ""
        half = [0] * 26

        # construim doar jumatatea
        for ch, cnt in freq.items():
            half[ord(ch) - ord('a')] = cnt // 2
            if cnt % 2:
                middle = ch

        # cate palindroame exista in total
        total = self.countArrangements(half)

        if k > total:
            return ""

        left = []

        halfLength = sum(half)

        # construim caracter cu caracter
        for _ in range(halfLength):

            for i in range(26):

                if half[i] == 0:
                    continue

                half[i] -= 1

                cnt = self.countArrangements(half)

                if cnt >= k:
                    left.append(chr(i + ord('a')))
                    break
                else:
                    k -= cnt
                    half[i] += 1

        return "".join(left) + middle + "".join(reversed(left))

    def countArrangements(self, half):

        total = sum(half)

        ans = 1

        for cnt in half:

            ans *= self.nCk(total, cnt)

            # nu avem nevoie de valori mai mari
            if ans >= self.MAX:
                return self.MAX

            total -= cnt

        return ans

    def nCk(self, n, k):

        ans = 1

        for i in range(1, min(k, n - k) + 1):

            ans = ans * (n - i + 1) // i

            if ans >= self.MAX:
                return self.MAX

        return ans