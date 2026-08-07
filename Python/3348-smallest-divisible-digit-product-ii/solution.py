from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),
    1: Counter(),
    2: Counter({2: 1}),
    3: Counter({3: 1}),
    4: Counter({2: 2}),
    5: Counter({5: 1}),
    6: Counter({2: 1, 3: 1}),
    7: Counter({7: 1}),
    8: Counter({2: 3}),
    9: Counter({3: 2}),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        need = self.getPrimeFactors(t)

        if need is None:
            return "-1"

        digitsNeeded = self.buildDigits(need)

        # not enough space for the required digits
        if sum(digitsNeeded.values()) > len(num):
            return "".join(d * cnt for d, cnt in digitsNeeded.items())

        # prime factors from the current number
        prefixFactors = Counter()
        for ch in num:
            prefixFactors += FACTOR_COUNTS[int(ch)]

        # find the first zero
        firstZero = len(num)
        for i, ch in enumerate(num):
            if ch == "0":
                firstZero = i
                break

        # current number already satisfies the conditions
        if firstZero == len(num) and need <= prefixFactors:
            return num

        # try changing digits from right to left
        for i in range(len(num) - 1, -1, -1):

            digit = int(num[i])

            prefixFactors -= FACTOR_COUNTS[digit]

            remaining = len(num) - i - 1

            if i > firstZero:
                continue

            # try every larger digit
            for bigger in range(digit + 1, 10):

                stillNeed = need - prefixFactors - FACTOR_COUNTS[bigger]

                digits = self.buildDigits(stillNeed)

                # check if the remaining positions are enough
                if sum(digits.values()) <= remaining:

                    ones = remaining - sum(digits.values())

                    ans = []
                    ans.append(num[:i])
                    ans.append(str(bigger))
                    ans.append("1" * ones)

                    for d, cnt in digits.items():
                        ans.append(d * cnt)

                    return "".join(ans)

        # build the smallest valid longer number
        digitsNeeded = self.buildDigits(need)

        ones = len(num) + 1 - sum(digitsNeeded.values())

        ans = []
        ans.append("1" * ones)

        for d, cnt in digitsNeeded.items():
            ans.append(d * cnt)

        return "".join(ans)

    def getPrimeFactors(self, t):

        cnt = Counter()

        # count prime factors
        for p in [2, 3, 5, 7]:
            while t % p == 0:
                cnt[p] += 1
                t //= p

        # impossible if another prime factor exists
        if t != 1:
            return None

        return cnt

    def buildDigits(self, need):

        c2 = need[2]
        c3 = need[3]
        c5 = need[5]
        c7 = need[7]

        # use as many 8s as possible
        cnt8, c2 = divmod(c2, 3)

        # use as many 9s as possible
        cnt9, c3 = divmod(c3, 2)

        # use as many 4s as possible
        cnt4, c2 = divmod(c2, 2)

        cnt6 = 0

        # combine one 2 and one 3 into 6
        if c2 == 1 and c3 == 1:
            cnt6 = 1
            c2 = 0
            c3 = 0

        # replace 4 and 3 with 6 and 2
        if c3 == 1 and cnt4 == 1:
            cnt4 = 0
            c3 = 0
            cnt6 += 1
            c2 += 1

        return {
            "2": c2,
            "3": c3,
            "4": cnt4,
            "5": c5,
            "6": cnt6,
            "7": c7,
            "8": cnt8,
            "9": cnt9,
        }