# 14. Longest Common Prefix

**Difficulty:** Easy

**Topics:** String, Trie

🔗 **Problem:** https://leetcode.com/problems/longest-common-prefix/

---

## Problem Summary

You are given an array of strings.

Find the longest prefix that is shared by every string in the array. If the strings do not share any common prefix, return an empty string.

---

## Example

### Example 1

**Input:**

```text
strs = ["flower","flow","flight"]
```

**Output:**

```text
"fl"
```

**Explanation:**

All three strings begin with `"fl"`, but the next character differs, so `"fl"` is the longest common prefix.

### Example 2

**Input:**

```text
strs = ["dog","racecar","car"]
```

**Output:**

```text
""
```

**Explanation:**

The strings do not share a common starting sequence, so the result is an empty string.

---

## Approach

The implemented solution builds the prefix one character at a time using the first string as a reference.

### Step 1

Handle the edge case where the input list is empty.

```python
if not strs:
    return ""
```

### Step 2

Initialize the current longest prefix.

```python
prefix = ""
```

### Step 3

Iterate through the characters of the first string.

For each position, create a candidate prefix.

```python
candidat = strs[0][:i + 1]
```

### Step 4

Check whether every string starts with the candidate prefix.

```python
if not word.startswith(candidat):
```

- If every string matches, update the current prefix.
- Otherwise, stop the search because any longer prefix would also fail.

### Step 5

Return the longest valid prefix found.

```python
return prefix
```

---

## Walkthrough

Consider:

```text
strs = ["flower","flow","flight"]
```

### Candidate `"f"`

| String | Starts With `"f"` |
| ------ | :---------------: |
| flower |         ✓         |
| flow   |         ✓         |
| flight |         ✓         |

Current prefix:

```text
"f"
```

---

### Candidate `"fl"`

| String | Starts With `"fl"` |
| ------ | :----------------: |
| flower |         ✓          |
| flow   |         ✓          |
| flight |         ✓          |

Current prefix:

```text
"fl"
```

---

### Candidate `"flo"`

| String | Starts With `"flo"` |
| ------ | :-----------------: |
| flower |          ✓          |
| flow   |          ✓          |
| flight |          ✗          |

The candidate is no longer common to every string, so the algorithm stops.

Final result:

```text
"fl"
```

---

## Complexity Analysis

Let:

- **n** be the number of strings.
- **m** be the length of the first string.

- **Time Complexity:** `O(n × m²)`
  - Up to `m` candidate prefixes are generated. Each candidate is created by slicing the first string and checked against all `n` strings using `startswith()`.

- **Space Complexity:** `O(m)`
  - Additional space is used to store the current candidate prefix and the final result.
