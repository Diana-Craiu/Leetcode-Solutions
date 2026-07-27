# 1464. Maximum Product of Two Elements in an Array

**Difficulty:** Easy

**Topics:** Array, Sorting

🔗 **Problem:** https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

---

## Problem Summary

You are given an integer array `nums`.

Choose two different elements from the array and compute:

```text
(nums[i] - 1) × (nums[j] - 1)
```

Return the maximum possible value of this expression.

---

## Example

### Example 1

**Input:**

```text
nums = [3,4,5,2]
```

**Output:**

```text
12
```

**Explanation:**

The largest two numbers are `5` and `4`.

Their product after subtracting `1` from each is:

```text
(5 - 1) × (4 - 1) = 4 × 3 = 12
```

### Example 2

**Input:**

```text
nums = [1,5,4,5]
```

**Output:**

```text
16
```

**Explanation:**

The two largest numbers are both `5`.

Their product is:

```text
(5 - 1) × (5 - 1) = 4 × 4 = 16
```

### Example 3

**Input:**

```text
nums = [3,7]
```

**Output:**

```text
12
```

**Explanation:**

The only possible pair is:

```text
(7 - 1) × (3 - 1) = 6 × 2 = 12
```

---

## Approach

The implemented solution sorts the array in descending order and uses the two largest values.

### Step 1

Sort the array from largest to smallest.

```python
result = sorted(nums, reverse=True)
```

The first two elements are the largest numbers.

### Step 2

Subtract `1` from each of the two largest values.

```python
a = result[0] - 1
b = result[1] - 1
```

### Step 3

Multiply the adjusted values.

```python
maximum = a * b
```

### Step 4

Return the computed product.

---

## Walkthrough

Consider:

```text
nums = [3,4,5,2]
```

### Sort the array

```text
[5,4,3,2]
```

### Select the two largest numbers

| Value | After Subtracting 1 |
| ----: | ------------------: |
|     5 |                   4 |
|     4 |                   3 |

### Compute the product

```text
4 × 3 = 12
```

Return:

```text
12
```

---

## Complexity Analysis

Let **n** be the length of the array.

- **Time Complexity:** `O(n log n)`
  - Sorting the array dominates the running time.

- **Space Complexity:** `O(n)`
  - The sorted copy of the array is stored separately.
