class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0

        freq = sorted(Counter(word).values(), reverse=True)

        for i, f in enumerate(freq):
            ans += f * (i // 8 + 1)

        return ans