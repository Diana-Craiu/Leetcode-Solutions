# 3536. Maximum Product of Two Digits

**Difficulty:** Easy

**Topics:** Math, Sorting

🔗 **Problem:** https://leetcode.com/problems/maximum-product-of-two-digits/

---

## Problem Summary

You are given a positive integer `n`.

Extract its digits and determine the maximum product that can be obtained by multiplying any two digits. If a digit appears multiple times, it may be used multiple times as long as each occurrence is available.

Return the largest possible product.

---

## Example

### Example 1

**Input:**

```text
n = 31
```

**Output:**

```text
3
```

**Explanation:**

The digits are:

```text
[3, 1]
```

The only possible product is:

```text
3 × 1 = 3
```

### Example 2

**Input:**

```text
n = 22
```

**Output:**

```text
4
```

**Explanation:**

The digits are:

```text
[2, 2]
```

The maximum product is:

```text
2 × 2 = 4
```

### Example 3

**Input:**

```text
n = 124
```

**Output:**

```text
8
```

**Explanation:**

The possible products are:

```text
1 × 2 = 2
1 × 4 = 4
2 × 4 = 8
```

The largest product is `8`.

---

## Approach

The implemented solution sorts the digits in descending order and multiplies the two largest digits.

### Step 1

Convert the integer into a string so that each digit can be processed individually.

### Step 2

Sort the digits in descending order.

```python
rezultat = "".join(sorted(str(n), reverse=True))
```

The first two characters now represent the two largest digits.

### Step 3

Convert those digits back to integers.

```python
a = int(rezultat[0])
b = int(rezultat[1])
```

### Step 4

Multiply the two largest digits and return the result.

```python
max_product = a * b
```

---

## Walkthrough

Consider:

```text
n = 124
```

### Convert to digits

```text
"124"
```

### Sort in descending order

```text
"421"
```

### Select the two largest digits

| Position | Digit |
| -------: | ----: |
|        0 |     4 |
|        1 |     2 |

### Compute the product

```text
4 × 2 = 8
```

Return:

```text
8
```

---

## Complexity Analysis

Let **d** be the number of digits in `n`.

- **Time Complexity:** `O(d log d)`
  - Sorting the digits dominates the running time.

- **Space Complexity:** `O(d)`
  - A string containing the sorted digits is created.
