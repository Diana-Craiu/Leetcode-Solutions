from collections import deque
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        window_sum=0
        left = 0
        max_len = 0
        n= len(chargeTimes)
        max_deque = deque()

        for right in range (n):
            window_sum += runningCosts[right]

            while max_deque and chargeTimes[max_deque[-1]] <= chargeTimes[right]:
                max_deque.pop()

            max_deque.append(right)


            while left <= right:
                k = right - left + 1
                max_val = chargeTimes[max_deque[0]]
                cost = max_val + k * window_sum

                if cost <= budget:
                    break

                if max_deque[0] == left:
                    max_deque.popleft()

                window_sum -= runningCosts[left]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len