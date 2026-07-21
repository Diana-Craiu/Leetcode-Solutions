# 3499. Maximize Active Section with Trade I

**Difficulty:** Medium

**Topics:** String, Greedy, Two Pointers

🔗 **Problem:** https://leetcode.com/problems/maximize-active-section-with-trade-i/

---

## Problem Summary

You are given a binary string where:

- `'1'` represents an active section.
- `'0'` represents an inactive section.

You may perform **at most one trade**. A trade consists of:

1. Converting a contiguous block of `'1'`s that is surrounded by `'0'`s into `'0'`s.
2. Converting a contiguous block of `'0'`s that is surrounded by `'1'`s into `'1'`s.

The string is considered to have an additional `'1'` at both ends when determining whether blocks are surrounded, but these extra characters are **not** counted in the final answer.

Return the maximum possible number of active sections after the optimal trade.

---

## Example

### Example 1

**Input:**

```text
s = "01"
```

**Output:**

```text
1
```

**Explanation:**

There is no valid block of `'1'`s surrounded by `'0'`s, so no trade can be performed. The number of active sections remains `1`.

### Example 2

**Input:**

```text
s = "0100"
```

**Output:**

```text
4
```

**Explanation:**

A valid trade converts the middle isolated `'1'` into `'0'`, merging the surrounding zero blocks. That merged block is then converted into `'1'`, making every section active.

### Example 3

**Input:**

```text
s = "1000100"
```

**Output:**

```text
7
```

**Explanation:**

Removing the isolated `'1'` joins the two neighboring zero blocks into one larger block, which is then converted into active sections.

### Example 4

**Input:**

```text
s = "01010"
```

**Output:**

```text
4
```

**Explanation:**

Choosing the middle isolated `'1'` merges the adjacent zero blocks, allowing them to be converted into active sections and producing four active sections.

---

## Approach

The implemented solution scans the string block by block and computes the largest possible increase in active sections.

### Step 1

Count the number of active sections already present.

```python
total_ones = s.count("1")
```

This forms the base answer before performing any trade.

### Step 2

Traverse the string while grouping consecutive equal characters into blocks.

For each block, determine:

- whether it is a block of `'0'`s or `'1'`s,
- and its length.

### Step 3

Whenever a zero block is encountered:

- If a previous zero block has already been seen, the block of `'1'`s between them could potentially be removed, merging both zero blocks.
- The resulting gain equals the combined size of the two zero blocks.

```python
max_gain = max(max_gain, left_zero_block + length)
```

### Step 4

Update the most recently seen zero block.

```python
left_zero_block = length
```

Continue until every block has been processed.

### Step 5

Return the original number of active sections plus the maximum gain found.

```python
return total_ones + max_gain
```

---

## Walkthrough

Consider:

```text
s = "01010"
```

Initial values:

```text
Total active sections = 2
```

The blocks are:

| Block | Length |
| ----- | -----: |
| 0     |      1 |
| 1     |      1 |
| 0     |      1 |
| 1     |      1 |
| 0     |      1 |

Process the blocks:

### First zero block

```text
left_zero_block = 1
```

No previous zero block exists yet.

### Middle zero block

Previous zero block:

```text
1
```

Current zero block:

```text
1
```

Possible gain:

```text
1 + 1 = 2
```

Maximum gain becomes:

```text
2
```

Update:

```text
left_zero_block = 1
```

### Last zero block

Again:

```text
gain = 1 + 1 = 2
```

The maximum gain remains:

```text
2
```

Final answer:

```text
total_ones + max_gain
= 2 + 2
= 4
```

---

## Complexity Analysis

Let **n** be the length of the string.

- **Time Complexity:** `O(n)`
  - The string is scanned once while grouping consecutive characters into blocks.

- **Space Complexity:** `O(1)`
  - Only a few variables are maintained regardless of the input size.
