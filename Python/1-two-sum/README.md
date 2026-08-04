# 1. Two Sum

**Difficulty:** Easy

**Topics:** Array, Hash Table

🔗 **Problem:** https://leetcode.com/problems/two-sum/

---

## Problem Summary

You are given an integer array `nums` and an integer `target`.

Find two different elements whose sum equals `target` and return their indices. It is guaranteed that exactly one valid pair exists, and the same element cannot be used twice.

The indices may be returned in any order.

---

## Example

### Example 1

**Input:**

```text
nums = [2,7,11,15]
target = 9
```

**Output:**

```text
[0,1]
```

**Explanation:**

The values at indices `0` and `1` are `2` and `7`.

Their sum is:

```text
2 + 7 = 9
```

which matches the target.

### Example 2

**Input:**

```text
nums = [3,2,4]
target = 6
```

**Output:**

```text
[1,2]
```

**Explanation:**

The values `2` and `4` add up to `6`, so their indices are returned.

### Example 3

**Input:**

```text
nums = [3,3]
target = 6
```

**Output:**

```text
[0,1]
```

**Explanation:**

The two elements both have value `3`, and together they equal the target.

---

## Approach

The implemented solution uses a brute-force approach by checking every possible pair of elements.

### Step 1

Iterate through the array using the first index.

```python
for i in range(len(nums)):
```

### Step 2

For each position, iterate through the remaining elements.

```python
for j in range(i + 1, len(nums)):
```

This ensures every unique pair is examined exactly once.

### Step 3

Compute the sum of the current pair.

```python
sum = nums[i] + nums[j]
```

### Step 4

If the sum equals the target, return the two indices immediately.

```python
if sum == target:
    return [i, j]
```

Since the problem guarantees exactly one valid solution, the search stops as soon as the matching pair is found.

---

## Walkthrough

Consider:

```text
nums = [2,7,11,15]
target = 9
```

### Compare pairs

| First Index | Second Index | Values  | Sum |
| ----------: | -----------: | ------- | --: |
|           0 |            1 | (2, 7)  |   9 |
|           0 |            2 | (2, 11) |  13 |
|           0 |            3 | (2, 15) |  17 |

The very first pair satisfies the condition:

```text
2 + 7 = 9
```

Therefore, the algorithm returns:

```text
[0,1]
```

No further comparisons are needed because the solution is guaranteed to be unique.

---

## Complexity Analysis

Let **n** be the length of the array.

- **Time Complexity:** `O(n²)`
  - In the worst case, every possible pair of elements is examined.

- **Space Complexity:** `O(1)`
  - Only a few variables are used regardless of the input size.
