# 3517. Smallest Palindromic Rearrangement I

**Difficulty:** Medium

**Topics:** String, Hash Table, Greedy, Counting

🔗 **Problem:** https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

---

## Problem Summary

You are given a string `s` that is already a palindrome.

Rearrange its characters to form another palindrome that is **lexicographically smallest** among all possible palindromic permutations.

Return the resulting palindrome.

---

## Example

### Example 1

**Input:**

```text
s = "z"
```

**Output:**

```text
"z"
```

**Explanation:**

The string contains only one character, so it is already the smallest possible palindrome.

### Example 2

**Input:**

```text
s = "babab"
```

**Output:**

```text
"abbba"
```

**Explanation:**

The character counts are:

```text
a → 2
b → 3
```

The smallest palindrome is formed by placing the smallest characters first in the left half, the odd-count character in the center, and mirroring the left half.

### Example 3

**Input:**

```text
s = "daccad"
```

**Output:**

```text
"acddca"
```

**Explanation:**

Sorting the character frequencies allows the left half to be built in lexicographical order, producing the smallest possible palindromic arrangement.

---

## Approach

The implemented solution counts the frequency of each character and constructs the palindrome from the outside toward the center.

### Step 1

Handle the special case where the string contains only one character.

```python
if len(s) == 1:
    return s
```

### Step 2

Count the occurrences of every character.

```python
freq = Counter(s)
```

### Step 3

Process the characters in alphabetical order.

For each character:

- If its frequency is odd, store it as the middle character.
- Append half of its occurrences to the left half of the palindrome.

```python
left += litera * (aparitii // 2)
```

### Step 4

Construct the right half by reversing the left half.

```python
right = left[::-1]
```

### Step 5

Concatenate the three parts.

```python
result = left + middle + right
```

Return the completed palindrome.

---

## Walkthrough

Consider:

```text
s = "babab"
```

### Count character frequencies

| Character | Frequency |
| --------: | --------: |
|         a |         2 |
|         b |         3 |

### Build the left half

Process characters alphabetically.

For `'a'`:

```text
2 // 2 = 1
```

Left:

```text
"a"
```

For `'b'`:

```text
3 // 2 = 1
```

Left:

```text
"ab"
```

Since `'b'` has an odd frequency, it becomes the middle character.

```text
Middle = "b"
```

### Build the right half

Reverse the left half.

```text
"ab" → "ba"
```

### Combine all parts

```text
Left   = "ab"
Middle = "b"
Right  = "ba"
```

Final palindrome:

```text
"abbba"
```

---

## Complexity Analysis

Let **n** be the length of the string.

- **Time Complexity:** `O(n)`
  - Counting the characters takes `O(n)`, and constructing the palindrome visits each character once. The alphabet size is fixed (26 lowercase letters), so sorting the frequency map is effectively constant time.

- **Space Complexity:** `O(n)`
  - The frequency map and the strings used to build the palindrome require additional space proportional to the output size.
