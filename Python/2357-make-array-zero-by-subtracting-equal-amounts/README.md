# 2357. Make Array Zero by Subtracting Equal Amounts

**Difficulty:** Easy

**Topics:** Array, Simulation

🔗 **Problem:** https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

---

## Problem Summary

Given an array of non-negative integers, perform operations that subtract the same positive value from every non-zero element. The chosen value must be less than or equal to the smallest non-zero element in the array.

Return the minimum number of operations required to make every element equal to `0`.

---

## Example

### Example 1

```text
Input:
nums = [1,5,0,3,5]

Output:
3
```

Explanation:

Initial array:

```text
[1,5,0,3,5]
```

**Operation 1**

- Smallest non-zero element = `1`
- Subtract `1` from every non-zero value.

```text
[0,4,0,2,4]
```

**Operation 2**

- Smallest non-zero element = `2`

```text
[0,2,0,0,2]
```

**Operation 3**

- Smallest non-zero element = `2`

```text
[0,0,0,0,0]
```

The array becomes entirely zero after **3 operations**.

---

### Example 2

```text
Input:
nums = [0]

Output:
0
```

The array is already zero, so no operations are required.

---

## Approach

This solution simulates the process described in the problem.

### Step 1

As long as the array contains at least one non-zero value:

- Find all positive numbers.
- Determine the smallest non-zero element.

### Step 2

Subtract this value from every non-zero element.

Elements that reach zero remain zero.

### Step 3

Increase the operation counter.

Repeat until every element becomes zero.

---

## Walkthrough

For the input:

```text
nums = [1,5,0,3,5]
```

| Operation | Smallest Non-Zero | Array After Operation |
| --------- | ----------------- | --------------------- |
| Start     | -                 | [1,5,0,3,5]           |
| 1         | 1                 | [0,4,0,2,4]           |
| 2         | 2                 | [0,2,0,0,2]           |
| 3         | 2                 | [0,0,0,0,0]           |

The answer is **3**.

---

## Complexity Analysis

Let **n** be the length of the array.

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n)`

The algorithm repeatedly scans the array until all elements become zero. Since the values are reduced over multiple iterations, the worst-case running time is quadratic.
