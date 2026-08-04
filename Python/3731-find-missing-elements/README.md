# 3731. Find Missing Elements

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sorting

🔗 **Problem:** https://leetcode.com/problems/find-missing-elements/

---

## Problem Summary

You are given an array of unique integers.

Originally, the array contained every integer within a continuous range, but some values may have been removed. The smallest and largest values from the original range are guaranteed to still be present.

Return all missing integers within that range in sorted order. If no numbers are missing, return an empty list.

---

## Example

### Example 1

**Input:**

```text
nums = [1,4,2,5]
```

**Output:**

```text
[3]
```

**Explanation:**

The smallest value is `1` and the largest is `5`, so the complete range is:

```text
[1,2,3,4,5]
```

The only missing number is:

```text
3
```

### Example 2

**Input:**

```text
nums = [7,8,6,9]
```

**Output:**

```text
[]
```

**Explanation:**

The complete range is:

```text
[6,7,8,9]
```

All numbers are present, so no values are missing.

### Example 3

**Input:**

```text
nums = [5,1]
```

**Output:**

```text
[2,3,4]
```

**Explanation:**

The complete range is:

```text
[1,2,3,4,5]
```

The missing integers are:

```text
[2,3,4]
```

---

## Approach

The implemented solution constructs the complete range of expected values and compares it with the given array.

### Step 1

Sort the input array.

```python
sorted_nums = sorted(nums)
```

This allows the smallest and largest values to be easily identified.

### Step 2

Determine the boundaries of the original range.

```python
first = sorted_nums[0]
last = sorted_nums[-1]
```

### Step 3

Generate the complete range of integers.

```python
full_range = list(range(first, last + 1))
```

### Step 4

Convert both collections into sets and compute their symmetric difference.

```python
set(nums) ^ set(full_range)
```

Since every element of `nums` belongs to the full range, the symmetric difference consists only of the missing integers.

### Step 5

Sort the resulting values and return them.

```python
missing_int = sorted(list(set(nums) ^ set(full_range)))
```

---

## Walkthrough

Consider:

```text
nums = [1,4,2,5]
```

### Sort the array

```text
[1,2,4,5]
```

### Determine the range

```text
First = 1
Last = 5
```

Generate the complete range:

```text
[1,2,3,4,5]
```

### Convert to sets

```text
nums       = {1,2,4,5}
full_range = {1,2,3,4,5}
```

### Compute the difference

```text
{1,2,4,5} ^ {1,2,3,4,5}
=
{3}
```

### Sort the result

```text
[3]
```

Return:

```text
[3]
```

---

## Complexity Analysis

Let **n** be the length of `nums`, and let **r** be the size of the complete range (`last - first + 1`).

- **Time Complexity:** `O(n log n + r)`
  - Sorting the array takes `O(n log n)`, generating the range and performing the set operations each take `O(r)`.

- **Space Complexity:** `O(r)`
  - The complete range and the sets require additional space proportional to the size of the range.
