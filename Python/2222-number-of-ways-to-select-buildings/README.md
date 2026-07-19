# 2222. Number of Ways to Select Buildings

**Difficulty:** Medium

**Topics:** String, Dynamic Programming, Prefix Sum, Counting

🔗 **Problem:** https://leetcode.com/problems/number-of-ways-to-select-buildings/

---

## Problem Summary

You are given a binary string where:

- `'0'` represents an office.
- `'1'` represents a restaurant.

Your task is to select **three buildings** while preserving their original order. The selected buildings must alternate in type, meaning the only valid patterns are:

- `010`
- `101`

Return the total number of valid ways to choose such three-building sequences.

---

## Example

### Example 1

**Input:**

```text
s = "001101"
```

**Output:**

```text
6
```

**Explanation:**

There are six valid selections whose building types form either `010` or `101`.

Valid index selections are:

```text
[0,2,4]
[0,3,4]
[1,2,4]
[1,3,4]
[2,4,5]
[3,4,5]
```

### Example 2

**Input:**

```text
s = "11100"
```

**Output:**

```text
0
```

**Explanation:**

No three selected buildings can form either `010` or `101`, so the answer is `0`.

---

## Approach

The implemented solution treats each building as the **middle** building of a potential pattern and counts how many valid buildings exist on both sides.

### Step 1

Maintain two arrays:

- `left_count` stores how many `0`s and `1`s have been seen so far.
- `right_count` stores how many `0`s and `1`s remain to the right.

Initially:

```python
left_count = [0, 0]
right_count = [s.count("0"), s.count("1")]
```

### Step 2

Iterate through the string one character at a time.

Before processing the current building, remove it from the right-side counts.

```python
right_count[digit] -= 1
```

### Step 3

Treat the current building as the middle building.

To create a valid pattern:

- If the middle is `0`, both neighboring buildings must be `1`.
- If the middle is `1`, both neighboring buildings must be `0`.

The opposite digit is computed using:

```python
opposite_digit = digit ^ 1
```

The number of valid selections using the current building as the middle is:

```python
left_count[opposite_digit] * right_count[opposite_digit]
```

Add this value to the final answer.

### Step 4

After processing the current position, update the left-side counts.

```python
left_count[digit] += 1
```

Continue until every building has been considered as the middle element.

---

## Walkthrough

Consider:

```text
s = "001101"
```

Initial counts:

```text
Left : 0 zeros, 0 ones
Right: 3 zeros, 3 ones
Answer = 0
```

| Position | Digit | Left Counts (0,1) | Right Counts (0,1) |  New Ways | Total |
| -------: | :---: | :---------------: | :----------------: | --------: | ----: |
|        0 |   0   |       (0,0)       |       (2,3)        | 0 × 3 = 0 |     0 |
|        1 |   0   |       (1,0)       |       (1,3)        | 0 × 3 = 0 |     0 |
|        2 |   1   |       (2,0)       |       (1,2)        | 2 × 1 = 2 |     2 |
|        3 |   1   |       (2,1)       |       (1,1)        | 2 × 1 = 2 |     4 |
|        4 |   0   |       (2,2)       |       (0,1)        | 2 × 1 = 2 |     6 |
|        5 |   1   |       (3,2)       |       (0,0)        | 3 × 0 = 0 |     6 |

The final answer is:

```text
6
```

---

## Complexity Analysis

Let **n** be the length of the string.

- **Time Complexity:** `O(n)`
  - The string is scanned once, while each iteration performs only constant-time operations.

- **Space Complexity:** `O(1)`
  - Only two fixed-size counting arrays are maintained regardless of the input size.
