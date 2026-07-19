# 2221. Find Triangular Sum of an Array

**Difficulty:** Medium

**Topics:** Array, Math, Simulation

🔗 **Problem:** https://leetcode.com/problems/find-triangular-sum-of-an-array/

---

## Problem Summary

You are given an array of digits.

Repeatedly replace the array with a new array where each element is the sum of two adjacent elements modulo `10`. Each iteration reduces the array length by one.

Continue this process until only one element remains, then return that remaining value as the triangular sum.

---

## Example

### Example 1

**Input:**

```text
nums = [1,2,3,4,5]
```

**Output:**

```text
8
```

**Explanation:**

The array is repeatedly reduced by replacing every pair of adjacent elements with their sum modulo `10` until only one value remains, which is `8`.

### Example 2

**Input:**

```text
nums = [5]
```

**Output:**

```text
5
```

**Explanation:**

Since the array already contains a single element, that value is the triangular sum.

---

## Approach

The implemented solution directly simulates the reduction process.

### Step 1

Store the current length of the array.

```python
n = len(nums)
```

### Step 2

While more than one element remains, generate the next row.

For every adjacent pair:

```python
(nums[i] + nums[i + 1]) % 10
```

Store the computed value in `newNums`.

### Step 3

As each value is computed, overwrite the corresponding position in `nums`.

```python
nums[i] = newNums[i]
```

This allows the beginning of `nums` to always contain the current row.

### Step 4

Reduce the effective array length by one after each iteration.

```python
n -= 1
```

Continue until only one element remains.

### Step 5

Return the first element of `nums`, which contains the final triangular sum.

---

## Walkthrough

Consider:

```text
nums = [1,2,3,4,5]
```

### Initial array

```text
[1,2,3,4,5]
```

### First iteration

Compute adjacent sums modulo `10`:

| Pair  | Value |
| ----- | ----: |
| 1 + 2 |     3 |
| 2 + 3 |     5 |
| 3 + 4 |     7 |
| 4 + 5 |     9 |

New row:

```text
[3,5,7,9]
```

---

### Second iteration

```text
(3+5)%10 = 8
(5+7)%10 = 2
(7+9)%10 = 6
```

New row:

```text
[8,2,6]
```

---

### Third iteration

```text
(8+2)%10 = 0
(2+6)%10 = 8
```

New row:

```text
[0,8]
```

---

### Fourth iteration

```text
(0+8)%10 = 8
```

Final row:

```text
[8]
```

Return:

```text
8
```

---

## Complexity Analysis

Let **n** be the length of the input array.

- **Time Complexity:** `O(n²)`
  - The array is reduced from size `n` to `1`, processing nearly all remaining elements during each iteration.

- **Space Complexity:** `O(n)`
  - A temporary array is created during each iteration, with a maximum size of `n - 1`.
