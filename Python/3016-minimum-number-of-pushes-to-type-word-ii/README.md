# 3016. Minimum Number of Pushes to Type Word II

**Difficulty:** Medium

**Topics:** Greedy, Hash Table, Sorting, String

🔗 **Problem:** https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

---

## Problem Summary

You are given a string `word` consisting of lowercase English letters.

You may freely remap the letters to the eight telephone keys (`2` through `9`), with each letter assigned to exactly one key. Unlike the first version of the problem, letters may appear multiple times in the word, so assigning the most frequently used letters to positions requiring fewer key presses minimizes the total typing cost.

Return the minimum number of key presses needed to type the entire word.

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

Each letter appears once, so they can all be assigned to the first position of different keys.

Total presses:

```text
1 + 1 + 1 + 1 + 1 = 5
```

### Example 2

**Input:**

```text
word = "xyzxyzxyzxyz"
```

**Output:**

```text
12
```

**Explanation:**

The three distinct letters each appear four times.

Assign each one to the first position of a key so every occurrence requires only one press.

```text
4 + 4 + 4 = 12
```

### Example 3

**Input:**

```text
word = "aabbccddeeffgghhiiiiii"
```

**Output:**

```text
24
```

**Explanation:**

The most frequent letter is assigned to a one-press position, while the remaining letters are placed in increasing order of typing cost to minimize the total number of key presses.

---

## Approach

The implemented solution counts how often each letter appears, sorts the frequencies in descending order, and assigns the most frequent letters to the cheapest keypad positions.

### Step 1

Count the frequency of every distinct letter.

```python
freq = sorted(Counter(word).values(), reverse=True)
```

Sorting in descending order ensures the most common letters are processed first.

### Step 2

Iterate through the sorted frequencies.

```python
for i, f in enumerate(freq):
```

The index determines the number of presses assigned to that letter.

### Step 3

Compute the typing cost.

Each group of eight letters requires one additional key press.

```python
ans += f * (i // 8 + 1)
```

The frequency is multiplied by the required number of presses because every occurrence of that letter contributes to the total.

### Step 4

Return the accumulated cost.

```python
return ans
```

---

## Walkthrough

Consider:

```text
word = "aabbccddeeffgghhiiiiii"
```

### Count the frequencies

| Letter | Frequency |
| -----: | --------: |
|      i |         6 |
|      a |         2 |
|      b |         2 |
|      c |         2 |
|      d |         2 |
|      e |         2 |
|      f |         2 |
|      g |         2 |
|      h |         2 |

### Sort the frequencies

```text
[6, 2, 2, 2, 2, 2, 2, 2, 2]
```

### Assign keypad costs

| Index | Frequency | Presses | Contribution |
| ----: | --------: | ------: | -----------: |
|     0 |         6 |       1 |            6 |
|     1 |         2 |       1 |            2 |
|     2 |         2 |       1 |            2 |
|     3 |         2 |       1 |            2 |
|     4 |         2 |       1 |            2 |
|     5 |         2 |       1 |            2 |
|     6 |         2 |       1 |            2 |
|     7 |         2 |       1 |            2 |
|     8 |         2 |       2 |            4 |

Total:

```text
6 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 4 = 24
```

The algorithm returns:

```text
24
```

---

## Complexity Analysis

Let **n** be the length of `word`, and let **m** be the number of distinct letters.

- **Time Complexity:** `O(n + m log m)`
  - Counting frequencies takes `O(n)`, and sorting the distinct frequencies takes `O(m log m)`. Since there are at most 26 lowercase letters, the sorting cost is effectively constant.

- **Space Complexity:** `O(m)`
  - The frequency table and sorted frequency list store one entry for each distinct letter.
