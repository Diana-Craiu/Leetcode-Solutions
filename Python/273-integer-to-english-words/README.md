# 273. Integer to English Words

**Difficulty:** Hard

**Topics:** Math, String, Recursion

🔗 **Problem:** https://leetcode.com/problems/integer-to-english-words/

---

## Problem Summary

Given a non-negative integer, convert it into its English words representation.

The output should correctly express the number using English words, including place values such as **Thousand**, **Million**, and **Billion**. The input can range from `0` up to `2³¹ - 1`.

---

## Example

### Example 1

**Input:**

```text
num = 123
```

**Output:**

```text
"One Hundred Twenty Three"
```

**Explanation:**

The number consists of one hundred followed by twenty-three, resulting in the phrase "One Hundred Twenty Three".

### Example 2

**Input:**

```text
num = 12345
```

**Output:**

```text
"Twelve Thousand Three Hundred Forty Five"
```

**Explanation:**

The number is split into the thousands group (`12`) and the remaining three-digit group (`345`), which are converted separately and combined.

### Example 3

**Input:**

```text
num = 1234567
```

**Output:**

```text
"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

**Explanation:**

The number is divided into million, thousand, and units groups. Each group is converted independently before appending its corresponding place value.

---

## Approach

The implemented solution converts the number in groups of three digits and processes each group independently.

### Step 1

Create two lookup tables:

- `ones_map` for numbers from `1` to `19`.
- `tens_map` for multiples of ten from `20` to `90`.

These maps provide the English word for each supported value.

### Step 2

Handle the special case where the input number is `0`.

```python
if num == 0:
    return "Zero"
```

### Step 3

Use the helper function `get_string()` to convert a three-digit number.

For each group:

- Convert the hundreds digit, if present.
- Convert the last two digits.
- Numbers below `20` are looked up directly.
- Otherwise, convert the tens digit first and then the ones digit if needed.

### Step 4

Repeatedly extract the last three digits using modulo `1000`.

```python
digits = num % 1000
```

Convert each group with `get_string()` and append the corresponding suffix:

- `""`
- `" Thousand"`
- `" Million"`
- `" Billion"`

### Step 5

The groups are processed from least significant to most significant, so the collected strings are reversed before joining them into the final answer.

---

## Walkthrough

Consider:

```text
num = 1234567
```

### Split into three-digit groups

| Group | Value | Suffix   |
| ----: | ----: | -------- |
|     1 |   567 |          |
|     2 |   234 | Thousand |
|     3 |     1 | Million  |

### Convert each group

#### Group 567

```text
Five Hundred Sixty Seven
```

#### Group 234

```text
Two Hundred Thirty Four Thousand
```

#### Group 1

```text
One Million
```

### Build the result

Groups are collected in this order:

```text
[
    "Five Hundred Sixty Seven",
    "Two Hundred Thirty Four Thousand",
    "One Million"
]
```

After reversing:

```text
[
    "One Million",
    "Two Hundred Thirty Four Thousand",
    "Five Hundred Sixty Seven"
]
```

Final output:

```text
One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
```

---

## Complexity Analysis

Let **d** be the number of digits in the input number.

- **Time Complexity:** `O(d)`
  - Each group of three digits is processed once, and the number of groups is proportional to the number of digits.

- **Space Complexity:** `O(1)`
  - The lookup tables and temporary lists have bounded size regardless of the input value.
