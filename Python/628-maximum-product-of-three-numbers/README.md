# 628. Maximum Product of Three Numbers

**Difficulty:** Easy

**Topics:** Array, Math, Sorting

🔗 **Problem:** https://leetcode.com/problems/maximum-product-of-three-numbers/

---

## Problem Summary

You are given an integer array `nums`, which may contain both positive and negative values.

Your task is to choose exactly three numbers whose product is as large as possible and return that maximum product.

---

## Example

### Example 1

**Input:**

```text
nums = [1,2,3]
```

**Output:**

```text
6
```

**Explanation:**

The only possible choice is:

```text
1 × 2 × 3 = 6
```

### Example 2

**Input:**

```text
nums = [1,2,3,4]
```

**Output:**

```text
24
```

**Explanation:**

Choosing the three largest numbers gives:

```text
2 × 3 × 4 = 24
```

### Example 3

**Input:**

```text
nums = [-1,-2,-3]
```

**Output:**

```text
-6
```

**Explanation:**

All three numbers must be selected, producing:

```text
(-1) × (-2) × (-3) = -6
```

---

## Approach

The implemented solution first sorts the array and then compares the two possible candidates for the maximum product.

### Step 1

Sort the array in ascending order.

```python
result = sorted(nums)
```

After sorting:

- The first two elements are the smallest values.
- The last three elements are the largest values.

### Step 2

Extract:

- The two smallest numbers.
- The three largest numbers.

```python
min1 = result[0]
min2 = result[1]

max1 = result[-1]
max2 = result[-2]
max3 = result[-3]
```

### Step 3

Compute the two possible maximum products.

The first possibility uses the two smallest numbers together with the largest number.

```python
negative_prod = min1 * min2 * max1
```

The second possibility uses the three largest numbers.

```python
positive_prod = max1 * max2 * max3
```

### Step 4

Return the larger of the two products.

```python
maximum_product = max(negative_prod, positive_prod)
```

---

## Walkthrough

Consider:

```text
nums = [-10,-10,5,2]
```

### Sort the array

```text
[-10,-10,2,5]
```

### Extract the required values

| Value | Number |
| ----: | -----: |
|  min1 |    -10 |
|  min2 |    -10 |
|  max1 |      5 |
|  max2 |      2 |
|  max3 |    -10 |

### Compute both candidate products

Using the two smallest and the largest:

```text
(-10) × (-10) × 5 = 500
```

Using the three largest values:

```text
5 × 2 × (-10) = -100
```

Choose the larger value:

```text
max(500, -100) = 500
```

Return:

```text
500
```

---

## Complexity Analysis

Let **n** be the length of the array.

- **Time Complexity:** `O(n log n)`
  - Sorting the array dominates the running time.

- **Space Complexity:** `O(n)`
  - The sorted copy of the array is stored separately.
