# 767. Reorganize String

**Difficulty:** Medium

**Topics:** String, Greedy, Hash Table

🔗 **Problem:** https://leetcode.com/problems/reorganize-string/

---

## Problem Summary

Given a string `s`, rearrange its characters so that no two adjacent characters are the same.

If such a rearrangement is possible, return any valid string. Otherwise, return an empty string.

---

## Example

### Example 1

```text
Input:
s = "aab"

Output:
"aba"
```

Explanation:

The two `'a'` characters are separated by `'b'`, so no adjacent characters are equal.

---

### Example 2

```text
Input:
s = "aaab"

Output:
""
```

Explanation:

The character `'a'` appears three times in a string of length four.

Since its frequency is greater than `(n + 1) / 2`, it is impossible to rearrange the string without placing two `'a'` characters next to each other.

---

## Approach

This solution uses a **greedy strategy** based on character frequencies.

### Step 1

Count the frequency of every character using a `Counter`.

```python
char_frequency = Counter(s)
```

---

### Step 2

Before constructing the answer, verify whether a valid rearrangement is possible.

If the most frequent character appears more than `(n + 1) // 2` times, no valid arrangement exists.

```python
if max_frequency > (string_length + 1) // 2:
    return ""
```

---

### Step 3

Create a result array with the same length as the input string.

Characters are inserted starting from the even indices (`0, 2, 4, ...`).

---

### Step 4

Process the characters in descending order of frequency.

For each character:

- place it in the current position;
- move two positions forward;
- once all even positions are filled, continue with the odd positions (`1, 3, 5, ...`).

This distribution keeps identical characters as far apart as possible.

---

## Walkthrough

Consider the input:

```text
s = "aab"
```

Character frequencies:

| Character | Frequency |
| --------- | --------: |
| a         |         2 |
| b         |         1 |

Result array:

```text
[_, _, _]
```

### Place `'a'`

```text
[a, _, a]
```

### Place `'b'`

Even positions are already filled, so continue with the first odd position.

```text
[a, b, a]
```

Final result:

```text
"aba"
```

No two adjacent characters are equal.

---

## Complexity Analysis

Let **n** be the length of the input string.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

The algorithm counts the character frequencies once and constructs the result in a single pass while using an additional array of size `n`.
