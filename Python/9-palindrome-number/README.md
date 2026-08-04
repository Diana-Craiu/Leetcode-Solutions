# 9. Palindrome Number

**Difficulty:** Easy

**Topics:** Math

🔗 **Problem:** https://leetcode.com/problems/palindrome-number/

---

## Problem Summary

Given an integer `x`, determine whether it is a palindrome.

A palindrome is a number that reads the same from left to right and from right to left. Negative numbers are not considered palindromes because the minus sign appears only at the beginning of the number.

Return `true` if the number is a palindrome; otherwise, return `false`.

---

## Example

### Example 1

**Input:**

```text
x = 121
```

**Output:**

```text
true
```

**Explanation:**

The number reads the same in both directions.

```text
121 → 121
```

### Example 2

**Input:**

```text
x = -121
```

**Output:**

```text
false
```

**Explanation:**

Reversing the number produces:

```text
121-
```

which is different from the original representation.

### Example 3

**Input:**

```text
x = 10
```

**Output:**

```text
false
```

**Explanation:**

Reversing the digits gives:

```text
01
```

which does not match the original number.

---

## Approach

The implemented solution converts the integer into a string and compares it with its reversed version.

### Step 1

Convert the integer to a string.

```python
str(x)
```

### Step 2

Create the reversed string using slicing.

```python
str(x)[::-1]
```

### Step 3

Compare the original and reversed strings.

```python
if str(x) == str(x)[::-1]:
```

- If they are equal, the number is a palindrome.
- Otherwise, it is not.

### Step 4

Return the corresponding boolean value.

---

## Walkthrough

Consider:

```text
x = 121
```

### Convert to a string

```text
"121"
```

### Reverse the string

```text
"121"[::-1]
```

Result:

```text
"121"
```

### Compare

```text
"121" == "121"
```

The comparison is:

```text
True
```

Therefore, the algorithm returns:

```text
true
```

---

## Complexity Analysis

Let **n** be the number of digits in the integer.

- **Time Complexity:** `O(n)`
  - Creating the reversed string and comparing it with the original both require linear time.

- **Space Complexity:** `O(n)`
  - An additional reversed string of length `n` is created.
