# 2213. Longest Substring of One Repeating Character

**Difficulty:** Hard

**Topics:** String, Segment Tree, Data Structure

🔗 **Problem:** https://leetcode.com/problems/longest-substring-of-one-repeating-character/

---

## Problem Summary

You are given a string `s` and a sequence of update queries.

Each query changes the character at a specified index of `s`. After every update, determine the length of the longest substring consisting of only one repeated character.

Return the longest length after each query.

---

## Example

### Example 1

**Input:**

```text
s = "babacc"
queryCharacters = "bcb"
queryIndices = [1,3,3]
```

**Output:**

```text
[3,3,4]
```

**Explanation:**

After the first update, the string becomes:

```text
"bbbacc"
```

The longest repeating substring is `"bbb"`, with length `3`.

After the second update:

```text
"bbbccc"
```

The longest repeating substring has length `3`.

After the third update:

```text
"bbbbcc"
```

The longest repeating substring is `"bbbb"`, with length `4`.

### Example 2

**Input:**

```text
s = "abyzz"
queryCharacters = "aa"
queryIndices = [2,1]
```

**Output:**

```text
[2,3]
```

**Explanation:**

After the first update, the string becomes:

```text
"abazz"
```

The longest repeating substring is `"zz"`, with length `2`.

After the second update, the string becomes:

```text
"aaazz"
```

The longest repeating substring is `"aaa"`, with length `3`.

---

## Approach

The implemented solution uses a **segment tree** to maintain information about every interval of the string.

Each tree node stores:

- the character at the left boundary;
- the character at the right boundary;
- the longest repeating prefix;
- the longest repeating suffix;
- the longest repeating substring inside the interval;
- the interval length.

### Step 1

Create a tree node for every individual character.

```python
def make_node(ch):
    return [ch, ch, 1, 1, 1, 1]
```

For a single character, the prefix, suffix, and longest repeating substring all have length `1`.

### Step 2

Build the segment tree recursively.

```python
def build(node, l, r):
```

Each internal node is created by merging its left and right children.

### Step 3

Merge two neighboring intervals.

```python
def merge(left, right):
```

The merge operation determines whether the character at the boundary is the same.

If both boundary characters match, the repeating prefix or suffix may extend across the boundary.

The best repeating substring can also cross the boundary:

```python
left_suffix + right_prefix
```

when the two boundary characters are equal.

### Step 4

Process each update.

```python
update(1, 0, n - 1, idx, ch)
```

Only the path from the updated position to the root needs to be recalculated.

Each affected node is merged again using the information from its two children.

### Step 5

After every update, the root represents the entire string.

The longest repeating substring length is stored at position `4` of the root node:

```python
ans.append(tree[1][4])
```

---

## Walkthrough

Consider:

```text
s = "babacc"
```

Initially, the segment tree represents the complete string.

### First query

```text
queryCharacters = "b"
queryIndices = [1]
```

Index `1` changes from:

```text
a → b
```

The string becomes:

```text
"bbbacc"
```

The update modifies the corresponding leaf and recalculates its ancestors.

At the root, the longest repeating substring has length:

```text
3
```

So the first answer is:

```text
3
```

### Second query

Index `3` changes:

```text
a → c
```

The string becomes:

```text
"bbbccc"
```

The segment tree is updated along the path containing index `3`.

The two largest repeating groups are:

```text
"bbb"
"ccc"
```

Therefore, the root reports:

```text
3
```

### Third query

Index `3` changes again:

```text
c → b
```

The string becomes:

```text
"bbbbcc"
```

The segment tree combines the adjacent `b` intervals.

The longest repeating substring is now:

```text
"bbbb"
```

with length:

```text
4
```

Therefore, the result is:

```text
[3,3,4]
```

---

## Complexity Analysis

Let **n** be the length of `s` and **k** be the number of queries.

- **Time Complexity:** `O(n + k log n)`
  - Building the segment tree takes `O(n)`. Each character update modifies `O(log n)` tree nodes, with constant-time merging.

- **Space Complexity:** `O(n)`
  - The segment tree contains `O(n)` nodes.
