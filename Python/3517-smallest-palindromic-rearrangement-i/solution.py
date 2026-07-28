from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:

        left=""
        right=""
        middle=""

        if len(s) == 1:
            return s

        freq = Counter(s)

        for litera, aparitii in sorted(freq.items()):
            if aparitii % 2 == 1:
                middle=litera
            
            left += litera*(aparitii//2)

        right = left[::-1]

        result=left+middle+right

        return result
            
