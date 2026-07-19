# 1081. Smallest Subsequence of Distinct Characters

**Difficulty:** Medium

**Topics:** Greedy, Stack, String

🔗 **Problem:** https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

---

## Problem Summary

Given a string `s`, construct the lexicographically smallest subsequence that contains every distinct character exactly once.

---

## Approach

This solution uses a **greedy algorithm** combined with a **monotonic stack**.

1. Store the last occurrence of every character in the string.
2. Traverse the string from left to right.
3. Skip characters that have already been added to the result.
4. While the current character is lexicographically smaller than the top of the stack **and** the character on the stack appears again later, remove it from the stack.
5. Push the current character onto the stack and mark it as visited.

This guarantees that:

- every character appears exactly once;
- the resulting subsequence is lexicographically minimal.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

where `n` is the length of the input string.
