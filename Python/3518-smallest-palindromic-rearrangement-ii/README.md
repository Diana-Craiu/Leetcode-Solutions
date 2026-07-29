# 3518. Smallest Palindromic Rearrangement II

**Difficulty:** Hard

**Topics:** String, Hash Table, Greedy, Combinatorics, Backtracking, Counting

🔗 **Problem:** https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

---

## Problem Summary

You are given a palindromic string `s` and an integer `k`.

Among all **distinct palindromic permutations** of `s`, return the **k-th lexicographically smallest** palindrome.

If fewer than `k` distinct palindromic permutations exist, return an empty string.

---

## Example

### Example 1

**Input:**

```text
s = "abba"
k = 2
```

**Output:**

```text
"baab"
```

**Explanation:**

The distinct palindromic rearrangements are:

```text
abba
baab
```

The second palindrome in lexicographical order is `"baab"`.

### Example 2

**Input:**

```text
s = "aa"
k = 2
```

**Output:**

```text
""
```

**Explanation:**

Only one distinct palindromic rearrangement exists, so there is no second palindrome.

### Example 3

**Input:**

```text
s = "bacab"
k = 1
```

**Output:**

```text
"abcba"
```

**Explanation:**

The smallest palindromic permutation in lexicographical order is `"abcba"`.

---

## Approach

The implemented solution builds the answer one character at a time while counting how many palindromic permutations remain for every possible choice.

### Step 1

Count the frequency of every character.

```python
freq = Counter(s)
```

For each character:

- Store half of its occurrences.
- If its frequency is odd, remember it as the middle character.

Only the left half of the palindrome needs to be constructed because the right half is determined automatically.

### Step 2

Compute the total number of distinct palindromic permutations.

This is done by the helper function `countArrangements()`, which calculates the number of distinct permutations of the remaining half using combinations.

If:

```python
k > total
```

return an empty string immediately.

### Step 3

Build the left half character by character.

For every position:

- Try each character from `'a'` to `'z'`.
- Temporarily use one occurrence of that character.
- Count how many palindromes can still be formed.

```python
cnt = self.countArrangements(half)
```

### Step 4

Decide whether to keep the chosen character.

- If `cnt >= k`, this character belongs at the current position.
- Otherwise, skip all those permutations.

```python
k -= cnt
```

Restore the character count and continue with the next letter.

### Step 5

After the left half is complete:

- Append the middle character (if one exists).
- Append the reverse of the left half.

The resulting string is the required palindrome.

---

## Walkthrough

Consider:

```text
s = "abba"
k = 2
```

### Character frequencies

| Character | Count |
| --------: | ----: |
|         a |     2 |
|         b |     2 |

Half counts:

```text
a → 1
b → 1
```

Middle:

```text
None
```

### Build the first position

Try `'a'`.

Remaining half:

```text
b → 1
```

Possible palindromes:

```text
1
```

Since:

```text
1 < k (2)
```

Skip these palindromes.

Update:

```text
k = 1
```

Restore `'a'`.

---

Try `'b'`.

Remaining half:

```text
a → 1
```

Possible palindromes:

```text
1
```

Since:

```text
1 ≥ k
```

Choose `'b'`.

Left half:

```text
"b"
```

### Build the second position

Only `'a'` remains.

Left half:

```text
"ba"
```

### Form the palindrome

```text
Left   = "ba"
Middle = ""
Right  = "ab"
```

Final answer:

```text
"baab"
```

---

## Complexity Analysis

Let:

- **n** be the length of the string.
- **m = n / 2** be the length of the left half.

- **Time Complexity:** `O(26 × m²)`
  - For each position in the left half, up to 26 characters are considered. Each candidate calls `countArrangements()`, which iterates through the character counts and computes combinations.

- **Space Complexity:** `O(m)`
  - The frequency arrays and the constructed left half require linear additional space.
