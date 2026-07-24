# 514. Number of Unique XOR Triplets II

**Difficulty:** Medium

**Topics:** Array, Bit Manipulation, Dynamic Programming

🔗 **Problem:** https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

---

## Problem Summary

You are given an integer array `nums`.

A XOR triplet is formed by selecting three elements (with indices `i ≤ j ≤ k`) and computing:

```text
nums[i] XOR nums[j] XOR nums[k]
```

Your task is to determine how many **distinct XOR values** can be produced from all possible triplets.

---

## Example

### Example 1

**Input:**

```text
nums = [1,3]
```

**Output:**

```text
2
```

**Explanation:**

The possible triplet XOR values are:

```text
1
3
1
3
```

The distinct results are:

```text
{1, 3}
```

Therefore, the answer is `2`.

### Example 2

**Input:**

```text
nums = [6,7,8,9]
```

**Output:**

```text
4
```

**Explanation:**

Every possible triplet produces one of the following values:

```text
{6, 7, 8, 9}
```

There are four unique XOR results.

---

## Approach

The implemented solution uses dynamic programming to keep track of every XOR value that can be formed after selecting one, two, and three numbers.

### Step 1

Create a DP buffer with four layers.

```python
buffer = [[False] * max_xor for _ in range(4)]
```

Each layer represents the XOR values obtainable after selecting:

- `0` numbers,
- `1` number,
- `2` numbers,
- `3` numbers.

Initially, selecting zero numbers produces XOR value `0`.

```python
buffer[0][0] = True
```

### Step 2

Repeat the transition three times.

For every XOR value already reachable in the current layer, try XOR-ing it with every number in `nums`.

```python
new[x ^ num] = True
```

This generates all reachable XOR values for the next layer.

### Step 3

Replace the next DP layer with the newly computed values.

After three iterations, `buffer[3]` contains every XOR value obtainable from three selections.

### Step 4

Count how many XOR values are marked as reachable.

```python
return sum(buffer[3])
```

---

## Walkthrough

Consider:

```text
nums = [1,3]
```

### Initial state

Only XOR `0` is possible before selecting any numbers.

| Selected Numbers | Reachable XOR Values |
| ---------------: | -------------------- |
|                0 | {0}                  |

---

### After selecting one number

Possible XOR values:

```text
0 XOR 1 = 1
0 XOR 3 = 3
```

Reachable values:

```text
{1,3}
```

---

### After selecting two numbers

Starting from `{1,3}`:

```text
1 XOR 1 = 0
1 XOR 3 = 2
3 XOR 1 = 2
3 XOR 3 = 0
```

Reachable values:

```text
{0,2}
```

---

### After selecting three numbers

Starting from `{0,2}`:

```text
0 XOR 1 = 1
0 XOR 3 = 3
2 XOR 1 = 3
2 XOR 3 = 1
```

Reachable values:

```text
{1,3}
```

The number of unique XOR triplet values is:

```text
2
```

---

## Complexity Analysis

Let:

- **n** be the length of `nums`.
- **M** be the maximum number of possible XOR states (`2048`).

- **Time Complexity:** `O(3 × M × n)` ≈ `O(M × n)`
  - For each of the three DP transitions, every reachable XOR state is combined with every element in the array.

- **Space Complexity:** `O(M)`
  - The DP buffer stores four layers of fixed size `2048`, which is constant with respect to the input size.
