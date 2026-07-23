# 3513. Number of Unique XOR Triplets I

**Difficulty:** Medium

**Topics:** Bit Manipulation, Array, Math

🔗 **Problem:** https://leetcode.com/problems/number-of-unique-xor-triplets-i/

---

## Problem Summary

You are given a permutation of the integers from `1` to `n`. A valid XOR triplet is formed by selecting three indices `i`, `j`, and `k` such that `i <= j <= k`, then computing:

`nums[i] XOR nums[j] XOR nums[k]`

The task is to determine how many distinct XOR values can be produced from every possible triplet.

---

## Example

### Example 1

**Input:**

```text
nums = [1,2]
```

**Output:**

```text
2
```

**Explanation:**

There are only four valid triplets because the indices may repeat while maintaining `i <= j <= k`. The resulting XOR values are either `1` or `2`, so there are two unique results.

---

### Example 2

**Input:**

```text
nums = [3,1,2]
```

**Output:**

```text
4
```

**Explanation:**

Evaluating all valid triplets produces the values `0`, `1`, `2`, and `3`. Since each value is distinct, the answer is `4`.

---

## Approach

The implementation relies on a mathematical observation about permutations of the numbers from `1` to `n`.

### Step 1

Determine the size of the permutation.

```python
n = len(nums)
```

### Step 2

Handle the small cases separately.

When the array contains fewer than three elements, every possible XOR result is simply one of the existing values, so the number of unique results equals `n`.

```python
if n < 3:
    return n
```

### Step 3

For `n >= 3`, use the known property that every XOR value in the range determined by the next power of two becomes achievable.

The number of distinct values is therefore the smallest power of two that is greater than `n`, which is computed as:

```python
return 1 << n.bit_length()
```

---

## Walkthrough

Consider the input:

```text
nums = [3,1,2]
```

1. Compute the array length.

| Variable | Value |
| -------- | ----: |
| `n`      |     3 |

2. Since `n >= 3`, the special case is skipped.

3. Compute:

```text
n.bit_length() = 2
```

4. Calculate:

```text
1 << 2 = 4
```

5. This matches the four distinct XOR values obtainable from all valid triplets:

| Unique XOR Values |
| ----------------- |
| 0                 |
| 1                 |
| 2                 |
| 3                 |

Therefore, the function returns:

```text
4
```

---

## Complexity Analysis

Let **n** be the length of `nums`.

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`
