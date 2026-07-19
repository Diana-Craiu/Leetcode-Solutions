# 1081. Smallest Subsequence of Distinct Characters

**Difficulty:** Medium

**Topics:** Greedy, Stack, String

🔗 **Problem:** https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

---

## Problem Summary

Given a string `s`, return the lexicographically smallest subsequence that contains each distinct character exactly once.

---

## Example

### Example 1

```text
Input:
s = "bcabc"

Output:
"abc"
```

Explanation:

- We must keep only one occurrence of each distinct character.
- The distinct characters are `a`, `b`, and `c`.
- Among all valid subsequences (`bac`, `bca`, `cab`, `abc`, ...), `"abc"` is the lexicographically smallest.

---

### Example 2

```text
Input:
s = "cbacdcbc"

Output:
"acdb"
```

Explanation:

- Every distinct character (`a`, `b`, `c`, `d`) must appear exactly once.
- The algorithm removes characters from the stack whenever they appear again later and replacing them produces a smaller lexicographical order.
- The final answer is `"acdb"`.

---

## Approach

The solution combines a **greedy strategy** with a **monotonic stack**.

### Step 1

Record the last occurrence of every character.

```python
last_occurrence = {char: index for index, char in enumerate(s)}
```

This allows us to know whether a character removed from the stack can still be added later.

### Step 2

Traverse the string from left to right.

If a character has already been included in the result, skip it.

### Step 3

Maintain a stack containing the current answer.

While:

- the stack is not empty;
- the top character is lexicographically larger than the current one;
- the top character appears again later;

remove it from the stack.

```python
while stack and stack[-1] > char and last_occurrence[stack[-1]] > index:
```

This is the greedy step that ensures the smallest possible answer.

### Step 4

Push the current character onto the stack and mark it as visited.

At the end, concatenate the stack to obtain the answer.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

where `n` is the length of the input string.
