# 3302. Find the Lexicographically Smallest Valid Sequence

**Difficulty:** Medium

**Topics:** String, Greedy, Two Pointers

🔗 **Problem:** https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

---

## Problem Summary

You are given two strings, `word1` and `word2`.

A valid sequence contains exactly `len(word2)` indices from `word1`, in strictly increasing order. The characters selected from `word1` must form a string that is either exactly equal to `word2` or can become equal to `word2` by changing at most one character.

The goal is to return the lexicographically smallest valid sequence of indices. If no valid sequence exists, return an empty array.

---

## Example

### Example 1

**Input:**

```text
word1 = "vbcca"
word2 = "abc"
```

**Output:**

```text
[0,1,2]
```

**Explanation:**

Selecting indices `[0,1,2]` gives:

```text
"vbc"
```

Changing the first character from `'v'` to `'a'` produces `"abc"`, so the sequence is valid.

### Example 2

**Input:**

```text
word1 = "bacdc"
word2 = "abc"
```

**Output:**

```text
[1,2,4]
```

**Explanation:**

The selected characters are:

```text
"adc"
```

Changing `'d'` to `'b'` produces `"abc"`. The indices `[1,2,4]` are the lexicographically smallest valid sequence.

### Example 3

**Input:**

```text
word1 = "aaaaaa"
word2 = "aaabc"
```

**Output:**

```text
[]
```

**Explanation:**

More than one character would need to be changed to transform any subsequence into `"aaabc"`, so no valid sequence exists.

### Example 4

**Input:**

```text
word1 = "abc"
word2 = "ab"
```

**Output:**

```text
[0,1]
```

**Explanation:**

The characters at indices `0` and `1` already form `"ab"`, so the sequence is valid without using a character change.

---

## Approach

The implemented solution uses a greedy scan combined with information about where the remaining characters of `word2` can be matched.

### Step 1

Build the `last` array.

```python
last = [-1] * len(word2)
```

`last[j]` stores the latest index in `word1` where `word2[j]` can be matched while scanning from right to left.

This helps determine whether the remaining suffix of `word2` can still be matched after using the one allowed character change.

### Step 2

Scan `word1` from right to left to populate `last`.

Whenever the current character matches the current character of `word2`, record its index and move to the previous character of `word2`.

### Step 3

Scan `word1` from left to right while constructing the answer.

A boolean variable tracks whether the single allowed character change is still available.

```python
canSkip = True
```

### Step 4

If the current character matches the next required character in `word2`, select its index immediately.

```python
if c == word2[j]:
    ans.append(i)
    j += 1
```

This greedily chooses the earliest possible index.

### Step 5

If the current character does not match, use the allowed character change only when the remaining part of `word2` can still be matched afterward.

```python
elif canSkip and (
    j == len(word2) - 1
    or i < last[j + 1]
):
```

If the condition holds, select the current index as the position where the character will be changed.

### Step 6

Continue until all characters of `word2` have been selected.

If all characters are matched, return the constructed sequence. Otherwise, return an empty array.

---

## Walkthrough

Consider:

```text
word1 = "bacdc"
word2 = "abc"
```

### Build the suffix information

Scanning from right to left identifies suitable positions for the remaining characters of `word2`.

The important information is that after selecting an index for `'a'` or `'b'`, there must still be enough positions to match the remaining suffix.

### Greedy scan

Start with:

```text
word2 = "abc"
j = 0
canSkip = True
```

#### Index 0

```text
word1[0] = 'b'
word2[0] = 'a'
```

The characters do not match.

Changing `'b'` to `'a'` is possible, but the greedy condition checks whether the remaining `"bc"` can still be matched afterward.

The scan continues until the earliest valid choice is found.

#### Index 1

```text
word1[1] = 'a'
word2[0] = 'a'
```

They match, so select index `1`.

```text
ans = [1]
j = 1
```

#### Index 2

```text
word1[2] = 'c'
word2[1] = 'b'
```

They do not match.

The one allowed change can be used here because the remaining character `'c'` can still be matched later.

Select index `2` and use the change:

```text
ans = [1,2]
canSkip = False
j = 2
```

#### Index 4

```text
word1[4] = 'c'
word2[2] = 'c'
```

The characters match, so select index `4`.

Final sequence:

```text
[1,2,4]
```

The selected characters are `"acc"`, and changing the middle `'c'` to `'b'` produces `"abc"`.

---

## Complexity Analysis

Let **n** be the length of `word1` and **m** be the length of `word2`.

- **Time Complexity:** `O(n + m)`
  - The `last` array is built with one right-to-left scan, followed by one left-to-right scan of `word1`.

- **Space Complexity:** `O(m)`
  - The `last` array and the resulting sequence require space proportional to `word2`.
