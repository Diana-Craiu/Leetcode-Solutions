# 140. Word Break II

**Difficulty:** Hard

**Topics:** String, Dynamic Programming, Backtracking, Memoization

🔗 **Problem:** https://leetcode.com/problems/word-break-ii/

---

## Problem Summary

Given a string `s` and a dictionary of valid words, return every possible sentence that can be formed by inserting spaces into `s` so that every resulting word belongs to the dictionary.

A dictionary word may be used multiple times if needed.

---

## Example

### Example 1

```text
Input:
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

Output:
[
  "cats and dog",
  "cat sand dog"
]
```

Explanation:

There are two valid ways to split the string into dictionary words:

- `cats and dog`
- `cat sand dog`

---

### Example 2

```text
Input:
s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]

Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
```

Explanation:

Multiple valid segmentations exist because different dictionary words can match the same portion of the string.

---

### Example 3

```text
Input:
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

Output:
[]
```

Explanation:

No valid segmentation exists, so the result is an empty list.

---

## Approach

This solution combines **backtracking** with **memoization**.

### Step 1

Convert the word dictionary into a set for efficient lookups.

```python
wordDict = set(wordDict)
```

---

### Step 2

Starting from a given index, try every possible substring.

Whenever a substring is found in the dictionary, recursively solve the remaining suffix of the string.

---

### Step 3

For every valid sentence returned by the recursive call:

- append the current word;
- insert a space if the remaining sentence is not empty.

This generates every possible sentence that starts from the current position.

---

### Step 4

Store the result for every starting index in a cache.

If the same suffix is encountered again, reuse the previously computed sentences instead of exploring it again.

---

## Walkthrough

Consider the input:

```text
s = "catsanddog"
```

Dictionary:

```text
["cat", "cats", "and", "sand", "dog"]
```

Starting at index `0`:

- `"cat"` is a valid word
  - Continue with `"sanddog"`
    - `"sand"` is valid
      - Continue with `"dog"`
        - `"dog"` is valid
          - End of string reached
          - Sentence: `"cat sand dog"`

- `"cats"` is a valid word
  - Continue with `"anddog"`
    - `"and"` is valid
      - Continue with `"dog"`
        - `"dog"` is valid
          - End of string reached
          - Sentence: `"cats and dog"`

Final result:

```text
[
  "cat sand dog",
  "cats and dog"
]
```

---

## Complexity Analysis

Let **n** be the length of the string.

- **Time Complexity:** Exponential in the worst case due to the number of possible valid sentence combinations.
- **Space Complexity:** `O(n + m)`, where `m` represents the total size of the cached results.

Memoization avoids recomputing the same suffix multiple times, significantly reducing the number of recursive calls compared to plain backtracking.
