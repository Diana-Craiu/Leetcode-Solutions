# 13. Roman to Integer

**Difficulty:** Easy

**Topics:** Hash Table, Math, String

🔗 **Problem:** https://leetcode.com/problems/roman-to-integer/

---

## Problem Summary

You are given a string representing a valid Roman numeral.

Roman numerals are normally written from largest to smallest, but certain pairs use subtractive notation. For example:

- `IV` represents `4`
- `IX` represents `9`
- `XL` represents `40`
- `XC` represents `90`
- `CD` represents `400`
- `CM` represents `900`

Convert the given Roman numeral into its corresponding integer value.

---

## Example

### Example 1

**Input:**

```text
s = "III"
```

**Output:**

```text
3
```

**Explanation:**

Each `I` represents `1`.

```text
1 + 1 + 1 = 3
```

### Example 2

**Input:**

```text
s = "LVIII"
```

**Output:**

```text
58
```

**Explanation:**

The numeral is interpreted as:

```text
L = 50
V = 5
III = 3
```

Total:

```text
50 + 5 + 3 = 58
```

### Example 3

**Input:**

```text
s = "MCMXCIV"
```

**Output:**

```text
1994
```

**Explanation:**

The numeral is split into:

```text
M  = 1000
CM = 900
XC = 90
IV = 4
```

Total:

```text
1000 + 900 + 90 + 4 = 1994
```

---

## Approach

The implemented solution scans the Roman numeral from left to right while comparing each symbol with the one that follows it.

### Step 1

Create a dictionary that maps every Roman numeral symbol to its integer value.

```python
numere = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
```

### Step 2

Initialize the result.

```python
numar = 0
```

### Step 3

Traverse the string up to the second-to-last character.

For each symbol:

- If its value is smaller than the next symbol, subtract it.
- Otherwise, add it.

```python
if numere[s[i]] < numere[s[i + 1]]:
    numar -= numere[s[i]]
else:
    numar += numere[s[i]]
```

This correctly handles both standard and subtractive notation.

### Step 4

After the loop, add the value of the final symbol.

```python
numar += numere[s[-1]]
```

### Step 5

Return the computed integer.

---

## Walkthrough

Consider:

```text
s = "MCMXCIV"
```

Process each character:

| Current | Next | Action | Total |
| :-----: | :--: | :----: | ----: |
|    M    |  C   | +1000  |  1000 |
|    C    |  M   |  -100  |   900 |
|    M    |  X   | +1000  |  1900 |
|    X    |  C   |  -10   |  1890 |
|    C    |  I   |  +100  |  1990 |
|    I    |  V   |   -1   |  1989 |

After the loop, add the final character:

```text
V = 5
```

Final result:

```text
1989 + 5 = 1994
```

Return:

```text
1994
```

---

## Complexity Analysis

Let **n** be the length of the Roman numeral.

- **Time Complexity:** `O(n)`
  - Each character is processed exactly once.

- **Space Complexity:** `O(1)`
  - The dictionary contains a fixed number of Roman numeral symbols.
