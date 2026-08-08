class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        ans = []

        # last[j] = the last index in word1 where word2[j] occurs
        last = [-1] * len(word2)

        # build last from right to left
        i = len(word1) - 1
        j = len(word2) - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        # we are allowed to change at most one character
        canSkip = True

        j = 0

        for i, c in enumerate(word1):

            # all characters from word2 have been found
            if j == len(word2):
                break

            # the current character matches
            if c == word2[j]:
                ans.append(i)
                j += 1

            # the current character does not match
            # use the only allowed change if the rest can still be matched
            elif canSkip and (
                j == len(word2) - 1
                or i < last[j + 1]
            ):
                canSkip = False
                ans.append(i)
                j += 1

        return ans if j == len(word2) else []