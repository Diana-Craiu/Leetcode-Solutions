# 2398. Maximum Number of Robots Within Budget

**Difficulty:** Hard

**Topics:** Array, Binary Search, Queue, Sliding Window, Monotonic Queue

🔗 **Problem:** https://leetcode.com/problems/maximum-number-of-robots-within-budget/

---

## Problem Summary

You are given two arrays of equal length:

- `chargeTimes`, where each value represents the one-time charging cost of a robot.
- `runningCosts`, where each value represents the running cost of a robot.

You may only choose **consecutive robots**. If `k` robots are selected, the total cost is calculated as:

```text
max(chargeTimes) + k × sum(runningCosts)
```

Return the maximum number of consecutive robots that can be operated without exceeding the given budget.

---

## Example

### Example 1

**Input:**

```text
chargeTimes = [3,6,1,3,4]
runningCosts = [2,1,3,4,5]
budget = 25
```

**Output:**

```text
3
```

**Explanation:**

Choosing the first three robots gives:

```text
max(3,6,1) + 3 × (2+1+3)
= 6 + 3 × 6
= 24
```

Since `24` does not exceed the budget, three robots can be operated together. No larger consecutive group satisfies the budget.

### Example 2

**Input:**

```text
chargeTimes = [11,12,19]
runningCosts = [10,8,7]
budget = 19
```

**Output:**

```text
0
```

**Explanation:**

Even operating a single robot exceeds the budget, so no valid group exists.

---

## Approach

The implemented solution combines a **sliding window** with a **monotonic deque**.

### Step 1

Maintain a sliding window using two pointers:

- `left`
- `right`

Also keep a running sum of the `runningCosts` inside the current window.

```python
window_sum += runningCosts[right]
```

### Step 2

Maintain a decreasing monotonic deque storing indices of `chargeTimes`.

Before inserting a new robot, remove all smaller or equal charge times from the back.

```python
while max_deque and chargeTimes[max_deque[-1]] <= chargeTimes[right]:
    max_deque.pop()
```

The front of the deque always stores the maximum charging cost in the current window.

### Step 3

For every window, compute:

```text
cost = maximum charge time
     + window size × sum of running costs
```

If the total cost exceeds the budget, shrink the window from the left.

When the leftmost robot leaves the window, remove it from the deque if necessary and subtract its running cost from the running sum.

### Step 4

After adjusting the window so that it satisfies the budget, update the maximum valid window size.

---

## Walkthrough

Consider:

```text
chargeTimes = [3,6,1,3,4]
runningCosts = [2,1,3,4,5]
budget = 25
```

### Right = 0

Window:

```text
[3]
```

- Max charge = 3
- Running sum = 2
- Cost = 3 + 1 × 2 = 5

Valid.

Maximum length:

```text
1
```

---

### Right = 1

Window:

```text
[3,6]
```

- Max charge = 6
- Running sum = 3
- Cost = 6 + 2 × 3 = 12

Valid.

Maximum length:

```text
2
```

---

### Right = 2

Window:

```text
[3,6,1]
```

- Max charge = 6
- Running sum = 6
- Cost = 6 + 3 × 6 = 24

Valid.

Maximum length:

```text
3
```

---

### Right = 3

Window:

```text
[3,6,1,3]
```

- Max charge = 6
- Running sum = 10
- Cost = 6 + 4 × 10 = 46

Budget exceeded.

Shrink the window from the left until the cost is within the budget.

---

### Right = 4

Repeat the same process:

- Expand the window.
- Update the deque.
- Shrink if necessary.

The largest valid window found throughout the traversal has length:

```text
3
```

---

## Complexity Analysis

Let **n** be the number of robots.

- **Time Complexity:** `O(n)`
  - Each robot enters and leaves the sliding window at most once, and every index is inserted into and removed from the deque at most once.

- **Space Complexity:** `O(n)`
  - The monotonic deque may contain up to `n` indices in the worst case.
