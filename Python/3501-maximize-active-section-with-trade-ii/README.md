# 3501. Maximize Active Section with Trade II

**Difficulty:** Hard

**Topics:** String, Array, Prefix Sum, Range Query, Sparse Table

🔗 **Problem:** https://leetcode.com/problems/maximize-active-section-with-trade-ii/

---

## Problem Summary

You are given a binary string where:

- `'1'` represents an active section.
- `'0'` represents an inactive section.

You are also given multiple queries, where each query specifies a substring of the original string.

For each query, you may perform **at most one trade** on the selected substring:

1. Convert one contiguous block of `'1'`s surrounded by `'0'`s into `'0'`s.
2. Then convert one contiguous block of `'0'`s surrounded by `'1'`s into `'1'`s.

Each queried substring is treated independently and is considered to be surrounded by an additional `'1'` on both ends.

Return the maximum number of active sections after the optimal trade for every query.

---

## Example

### Example 1

**Input:**

```text
s = "01"
queries = [[0,1]]
```

**Output:**

```text
[1]
```

**Explanation:**

No valid trade exists because there is no block of `'1'`s surrounded by `'0'`s.

### Example 2

**Input:**

```text
s = "0100"
queries = [[0,3],[0,2],[1,3],[2,3]]
```

**Output:**

```text
[4,3,1,1]
```

**Explanation:**

Each query is processed independently. Depending on the selected substring, a trade may merge neighboring zero blocks and increase the number of active sections.

### Example 3

**Input:**

```text
s = "1000100"
queries = [[1,5],[0,6],[0,4]]
```

**Output:**

```text
[6,7,2]
```

**Explanation:**

The optimal trade differs for each substring. The best possible number of active sections is returned for every query separately.

### Example 4

**Input:**

```text
s = "01010"
queries = [[0,3],[1,4],[1,3]]
```

**Output:**

```text
[4,4,2]
```

**Explanation:**

Only queries containing a removable block of `'1'`s can benefit from a trade.

---

## Approach

The implemented solution preprocesses the string into zero-blocks and answers each query using a combination of block information and a Sparse Table for fast range maximum queries.

### Step 1

Count the total number of active sections.

```python
ones = s.count("1")
```

This serves as the base value before applying any trade.

### Step 2

Traverse the string and group consecutive `'0'`s into blocks.

For every zero block, store:

- its starting index,
- its length.

Additionally, build `groupId`, which maps every position in the string to its corresponding zero-block index (or `-1` if the position is not inside a zero block).

### Step 3

For every pair of adjacent zero blocks, compute their combined length.

```python
merge[i] = groups[i][1] + groups[i + 1][1]
```

This represents the gain obtained by removing the `'1'` block between those two zero blocks.

### Step 4

Build a Sparse Table over the `merge` array.

The Sparse Table supports efficient maximum range queries, allowing each query to quickly find the best merge completely contained within its substring.

### Step 5

Process every query independently.

For each substring:

- Determine partial zero blocks touching the left and right boundaries.
- Query the Sparse Table for fully contained adjacent zero-block pairs.
- Check edge cases where a partial boundary block can be merged with a neighboring full block.
- Compute the largest possible gain and add it to the original number of active sections.

Append the resulting maximum to the answer array.

---

## Walkthrough

Consider:

```text
s = "1000100"
```

Zero blocks are:

| Block | Start | Length |
| ----: | ----: | -----: |
|     0 |     1 |      3 |
|     1 |     5 |      2 |

The merge array becomes:

```text
[5]
```

A Sparse Table is built on this array.

Now process the query:

```text
[0,6]
```

The substring contains both zero blocks entirely.

Possible gain:

```text
3 + 2 = 5
```

Original active sections:

```text
2
```

Maximum result:

```text
2 + 5 = 7
```

For a query such as:

```text
[0,4]
```

Only one zero block is completely contained, so no valid merge exists.

The answer remains:

```text
2
```

Each query follows the same procedure, combining information from boundary blocks and the Sparse Table to determine the optimal trade.

---

## Complexity Analysis

Let:

- **n** be the length of the string.
- **q** be the number of queries.

- **Preprocessing Time:** `O(n log n)`
  - Building the zero-block information, merge array, and Sparse Table.

- **Query Time:** `O(1)`
  - Each query performs only constant-time calculations and at most one Sparse Table lookup.

- **Space Complexity:** `O(n log n)`
  - The zero-block arrays and Sparse Table require additional memory proportional to the input size.
