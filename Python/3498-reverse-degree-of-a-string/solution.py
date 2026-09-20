class Solution:
    def reverseDegree(self, s: str) -> int:
        letter_count = dict(zip(string.ascii_lowercase, range(26, 0, -1)))
        sum=0
        for index, i in enumerate(s, start=1):
            sum=sum+(letter_count[i] * index)

        return sum
