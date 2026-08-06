# 3345. Smallest Divisible Digit Product I

**Difficulty:** Easy

**Topics:** Math, Brute Force

🔗 **Problem:** https://leetcode.com/problems/smallest-divisible-digit-product-i/

---

## Problem Summary

You are given two integers, `n` and `t`.

Find the smallest integer greater than or equal to `n` whose product of digits is divisible by `t`.

Return the first number that satisfies this condition.

---

## Example

### Example 1

**Input:**

```text
n = 10
t = 2
```

**Output:**

```text
10
```

**Explanation:**

The digits of `10` are `1` and `0`.

Their product is:

```text
1 × 0 = 0
```

Since `0` is divisible by `2`, `10` is already the smallest valid number.

### Example 2

**Input:**

```text
n = 15
t = 3
```

**Output:**

```text
16
```

**Explanation:**

For `15`:

```text
1 × 5 = 5
```

which is not divisible by `3`.

For `16`:

```text
1 × 6 = 6
```

Since `6` is divisible by `3`, the answer is `16`.

---

## Approach

The implemented solution checks consecutive numbers starting from `n` until it finds one whose digit product is divisible by `t`.

### Step 1

Compute the product of the digits of the current number.

```python
rezultat = prod(int(c) for c in str(n))
```

### Step 2

Repeatedly test whether the digit product is divisible by `t`.

```python
if rezultat % t == 0:
```

If it is, return the current number.

### Step 3

Otherwise, increment the number.

```python
n = n + 1
```

### Step 4

Recompute the digit product for the new number.

```python
rezultat = prod(int(c) for c in str(n))
```

Continue until a valid number is found.

---

## Walkthrough

Consider:

```text
n = 15
t = 3
```

### Check 15

Digits:

```text
1, 5
```

Product:

```text
1 × 5 = 5
```

Since:

```text
5 % 3 ≠ 0
```

Increment:

```text
n = 16
```

---

### Check 16

Digits:

```text
1, 6
```

Product:

```text
1 × 6 = 6
```

Now:

```text
6 % 3 = 0
```

The condition is satisfied.

Return:

```text
16
```

---

## Complexity Analysis

Let **d** be the maximum number of digits examined, and let **k** be the number of integers checked before finding a valid answer.

- **Time Complexity:** `O(k × d)`
  - For each candidate number, the algorithm computes the product of its digits.

- **Space Complexity:** `O(d)`
  - Converting the current number to a string requires space proportional to its number of digits.
