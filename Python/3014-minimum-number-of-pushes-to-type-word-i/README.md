# 3014. Minimum Number of Pushes to Type Word I

**Difficulty:** Easy

**Topics:** Greedy, Math, String

🔗 **Problem:** https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

---

## Problem Summary

You are given a string `word` containing distinct lowercase English letters.

You may remap the letters to the eight telephone keys (`2` through `9`) in any way you choose, provided each letter is assigned to exactly one key. The goal is to minimize the total number of key presses needed to type the entire word.

Return the minimum total number of key presses.

---

## Example

### Example 1

**Input:**

```text
word = "abcde"
```

**Output:**

```text
5
```

**Explanation:**

Since there are only five distinct letters, each can be assigned as the first letter on a different key.

Each character requires one press:

```text
1 + 1 + 1 + 1 + 1 = 5
```

### Example 2

**Input:**

```text
word = "xycdefghij"
```

**Output:**

```text
12
```

**Explanation:**

The first eight letters can each occupy the first position on a key and require one press.

The remaining two letters become the second letter on a key, requiring two presses each.

```text
8 × 1 + 2 × 2 = 12
```

---

## Approach

The implemented solution assigns the letters to key positions in the order of increasing typing cost.

Since there are **8 available keys**, the first eight letters each require one press, the next eight require two presses, and so on.

### Step 1

Initialize the answer.

```python
ans = 0
```

### Step 2

Iterate through every character position in the word.

```python
for i in range(len(word)):
```

### Step 3

Determine how many presses are needed for the current letter.

Every group of eight letters increases the required number of presses by one.

```python
ans += i // 8 + 1
```

### Step 4

Return the accumulated total.

```python
return ans
```

---

## Walkthrough

Consider:

```text
word = "xycdefghij"
```

The word contains **10** distinct letters.

| Letter Position | Required Presses |
| --------------: | ---------------: |
|               0 |                1 |
|               1 |                1 |
|               2 |                1 |
|               3 |                1 |
|               4 |                1 |
|               5 |                1 |
|               6 |                1 |
|               7 |                1 |
|               8 |                2 |
|               9 |                2 |

Total presses:

```text
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 = 12
```

The algorithm returns:

```text
12
```

---

## Complexity Analysis

Let **n** be the length of `word`.

- **Time Complexity:** `O(n)`
  - The solution processes each character exactly once.

- **Space Complexity:** `O(1)`
  - Only a few variables are used regardless of the input size.
