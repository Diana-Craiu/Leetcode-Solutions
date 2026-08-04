class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            candidat = strs[0][:i+1]

            ok = True

            for word in strs:
                if not word.startswith(candidat):
                    ok = False
                    break

            if ok:
                prefix = candidat
            else:
                break

        return prefix