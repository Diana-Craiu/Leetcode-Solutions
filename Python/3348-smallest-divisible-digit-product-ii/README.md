# 3348. Smallest Divisible Digit Product II

**Difficulty:** Hard

**Topics:** String, Greedy, Math, Prime Factorization, Counting

🔗 **Problem:** https://leetcode.com/problems/smallest-divisible-digit-product-ii/

---

## Problem Summary

You are given a positive integer represented as a string `num` and an integer `t`.

Find the smallest **zero-free** number that is greater than or equal to `num` such that the product of its digits is divisible by `t`.

A valid number:

- cannot contain the digit `0`,
- must be at least as large as `num`,
- must have a digit product divisible by `t`.

If no such number exists, return `"-1"`.

---

## Example

### Example 1

**Input:**

```text
num = "1234"
t = 256
```

**Output:**

```text
"1488"
```

**Explanation:**

The product of the digits is:

```text
1 × 4 × 8 × 8 = 256
```

which is divisible by `256`, and `"1488"` is the smallest valid number meeting all requirements.

### Example 2

**Input:**

```text
num = "12355"
t = 50
```

**Output:**

```text
"12355"
```

**Explanation:**

The number is already zero-free.

Its digit product is:

```text
1 × 2 × 3 × 5 × 5 = 150
```

Since `150` is divisible by `50`, the original number is returned.

### Example 3

**Input:**

```text
num = "11111"
t = 26
```

**Output:**

```text
"-1"
```

**Explanation:**

The prime factor `13` cannot be produced using decimal digits, making the required product impossible.

---

## Approach

The implemented solution combines **prime factorization**, a **greedy digit construction**, and a **right-to-left search** to build the smallest valid number.

### Step 1

Factorize `t` into the only prime factors that can appear in digit products:

- `2`
- `3`
- `5`
- `7`

```python
need = self.getPrimeFactors(t)
```

If any other prime factor remains, no valid answer exists.

### Step 2

Convert the required prime factors into the smallest collection of digits.

The helper function `buildDigits()` greedily compresses factors by using larger digits whenever beneficial.

For example:

- three `2`s → `8`
- two `3`s → `9`
- two `2`s → `4`
- one `2` and one `3` → `6`

This minimizes the number of required digits.

### Step 3

Count the prime factors contributed by every prefix of the current number.

Each digit contributes fixed prime factors stored in:

```python
FACTOR_COUNTS
```

This allows the remaining required factors to be computed efficiently while scanning the number.

### Step 4

If the original number:

- contains no zero, and
- already contains all required prime factors,

return it immediately.

### Step 5

Otherwise, process the digits from right to left.

For every position:

- remove the current digit's contribution,
- try replacing it with every larger digit,
- compute the remaining required prime factors,
- determine whether they can fit into the remaining positions.

If they can:

- keep the unchanged prefix,
- place the chosen larger digit,
- fill unused positions with `'1'`,
- append the required digits in increasing order.

The first successful construction is the smallest valid answer.

### Step 6

If no number of the same length is possible, construct the smallest valid number with one additional digit.

The extra positions are filled with `'1'`, followed by the minimum required digits.

---

## Walkthrough

Consider:

```text
num = "1234"
t = 256
```

### Prime factorization

```text
256 = 2⁸
```

Required factors:

| Prime | Count |
| ----: | ----: |
|     2 |     8 |

### Build required digits

Eight factors of `2` become:

```text
8 × 8 × 4
```

since:

```text
8 = 2³
8 = 2³
4 = 2²
```

Together they contribute:

```text
2³ × 2³ × 2² = 2⁸
```

### Try modifying the number

The algorithm scans from right to left.

Replacing the final digit allows the suffix to be rebuilt.

The smallest valid construction becomes:

```text
1488
```

Digit product:

```text
1 × 4 × 8 × 8 = 256
```

Since this is divisible by `256` and no smaller valid number exists, the answer is:

```text
1488
```

---

## Complexity Analysis

Let:

- **n** be the length of `num`.

- **Time Complexity:** `O(n)`
  - The string is scanned a constant number of times, and each position tries at most nine replacement digits. All helper operations work on a fixed set of prime factors and digit types.

- **Space Complexity:** `O(n)`
  - Additional space is used for the factor counters and for constructing the resulting string.
