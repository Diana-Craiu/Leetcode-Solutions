import itertools

class SparseTable:
    def __init__(self, nums):
        n = len(nums)
        self.st = [nums]

        k = 1
        while (1 << k) <= n:
            row = []
            for i in range(n - (1 << k) + 1):
                row.append(max(
                    self.st[k - 1][i],
                    self.st[k - 1][i + (1 << (k - 1))]
                ))
            self.st.append(row)
            k += 1

    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries):
        ones = s.count("1")

        groups = []
        groupId = []

        for i, c in enumerate(s):
            if c == "0":
                if i and s[i - 1] == "0":
                    groups[-1][1] += 1
                else:
                    groups.append([i, 1])
            groupId.append(len(groups) - 1)

        if not groups:
            return [ones] * len(queries)

        merge = [
            groups[i][1] + groups[i + 1][1]
            for i in range(len(groups) - 1)
        ]

        st = SparseTable(merge)

        ans = []

        for l, r in queries:

            left = -1 if groupId[l] == -1 else \
                groups[groupId[l]][1] - (l - groups[groupId[l]][0])

            right = -1 if groupId[r] == -1 else \
                r - groups[groupId[r]][0] + 1

            start = groupId[l] + 1
            end = groupId[r] if s[r] == "1" else groupId[r] - 1

            best = ones

            if s[l] == "0" and s[r] == "0" and groupId[l] + 1 == groupId[r]:
                best = max(best, ones + left + right)

            elif start <= end - 1:
                best = max(best, ones + st.query(start, end - 1))

            if s[l] == "0" and groupId[l] + 1 <= end:
                best = max(best, ones + left + groups[groupId[l] + 1][1])

            if s[r] == "0" and groupId[l] < groupId[r] - 1:
                best = max(best, ones + right + groups[groupId[r] - 1][1])

            ans.append(best)

        return ans