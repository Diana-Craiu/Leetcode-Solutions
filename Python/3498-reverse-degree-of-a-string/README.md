# 3498. Reverse Degree of a String

**Difficulty:** Easy

**Topics:** String, Hash Table, Simulation

🔗 **Problem:** https://leetcode.com/problems/reverse-degree-of-a-string/

---

## Problem Summary

Given a lowercase string `s`, calculate its reverse degree.

Each character is assigned a value based on its position in the reversed alphabet:

- `'a' = 26`
- `'b' = 25`
- ...
- `'z' = 1`

For every character, multiply its reversed-alphabet value by its position in the string (1-indexed). The reverse degree is the sum of all these products.

---

## Example

### Example 1

**Input:**

```text
s = "abc"
```

**Output:**

```text
148
```

**Explanation:**

Character values in the reversed alphabet:

| Character | Value | Position | Product |
| --------- | ----- | -------- | ------- |
| a         | 26    | 1        | 26      |
| b         | 25    | 2        | 50      |
| c         | 24    | 3        | 72      |

Total:

```text
26 + 50 + 72 = 148
```

### Example 2

**Input:**

```text
s = "zaza"
```

**Output:**

```text
160
```

**Explanation:**

| Character | Value | Position | Product |
| --------- | ----- | -------- | ------- |
| z         | 1     | 1        | 1       |
| a         | 26    | 2        | 52      |
| z         | 1     | 3        | 3       |
| a         | 26    | 4        | 104     |

Total:

```text
1 + 52 + 3 + 104 = 160
```

---

## Approach

The solution creates a mapping between each lowercase letter and its position in the reversed alphabet.

### Step 1

Build a dictionary where:

```python
letter_count = dict(zip(string.ascii_lowercase, range(26, 0, -1)))
```

This produces mappings such as:

```text
a → 26
b → 25
...
z → 1
```

### Step 2

Iterate through the string while keeping track of each character's 1-based position.

```python
for index, i in enumerate(s, start=1):
```

### Step 3

For each character, multiply:

```python
letter_count[i] * index
```

and add the result to the running total.

### Step 4

Return the accumulated sum after processing all characters.

---

## Walkthrough

Consider:

```text
s = "abc"
```

The reversed alphabet values are:

```text
a → 26
b → 25
c → 24
```

Process each character:

| Position | Character | Value | Contribution |
| -------- | --------- | ----- | ------------ |
| 1        | a         | 26    | 26 × 1 = 26  |
| 2        | b         | 25    | 25 × 2 = 50  |
| 3        | c         | 24    | 24 × 3 = 72  |

Running total:

```text
26 + 50 + 72 = 148
```

The final answer is:

```text
148
```

---

## Complexity Analysis

Let **n** be the length of the string.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

The dictionary contains a fixed number of 26 entries, and each character is processed exactly once.
