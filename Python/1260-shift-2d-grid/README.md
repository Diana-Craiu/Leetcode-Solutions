# 1260. Shift 2D Grid

**Difficulty:** Easy

**Topics:** Array, Matrix, Simulation

🔗 **Problem:** https://leetcode.com/problems/shift-2d-grid/

---

## Problem Summary

You are given an `m × n` grid and an integer `k`.

One shift operation moves every element one position forward in row-major order:

- Each element moves one column to the right.
- The last element of a row becomes the first element of the next row.
- The bottom-right element wraps around to the top-left corner.

Return the grid after performing the shift operation `k` times.

---

## Example

### Example 1

**Input:**

```text
grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
k = 1
```

**Output:**

```text
[[9,1,2],
 [3,4,5],
 [6,7,8]]
```

**Explanation:**

Each element moves one position forward, and the last element (`9`) wraps around to the beginning of the grid.

### Example 2

**Input:**

```text
grid = [[3,8,1,9],
        [19,7,2,5],
        [4,6,11,10],
        [12,0,21,13]]
k = 4
```

**Output:**

```text
[[12,0,21,13],
 [3,8,1,9],
 [19,7,2,5],
 [4,6,11,10]]
```

**Explanation:**

Shifting four times moves the last row to the front while preserving the order of the remaining elements.

### Example 3

**Input:**

```text
grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
k = 9
```

**Output:**

```text
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```

**Explanation:**

The grid contains `9` elements, so shifting `9` times returns it to its original configuration.

---

## Approach

The implemented solution treats the 2D grid as a single one-dimensional array.

### Step 1

Determine:

- Number of rows.
- Number of columns.
- Total number of elements.

```python
rows = len(grid)
cols = len(grid[0])
total = rows * cols
```

### Step 2

Reduce the number of shifts using modulo.

```python
k %= total
```

Since shifting by the total number of elements restores the original grid, only the remaining shifts need to be performed.

### Step 3

Create a new grid with the same dimensions to store the shifted values.

### Step 4

For every element:

- Convert its `(row, column)` position into a one-dimensional index.

```python
index = i * cols + j
```

- Compute its new position after shifting.

```python
new_index = (index + k) % total
```

### Step 5

Convert the new one-dimensional index back into row and column coordinates.

```python
new_row = new_index // cols
new_col = new_index % cols
```

Place the current value into its new position in the result grid.

---

## Walkthrough

Consider:

```text
grid =
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

k = 1
```

The grid contains:

```text
3 × 3 = 9 elements
```

### Convert positions to linear indices

| Value | Original Index | New Index |
| ----: | -------------: | --------: |
|     1 |              0 |         1 |
|     2 |              1 |         2 |
|     3 |              2 |         3 |
|     4 |              3 |         4 |
|     5 |              4 |         5 |
|     6 |              5 |         6 |
|     7 |              6 |         7 |
|     8 |              7 |         8 |
|     9 |              8 |         0 |

### Convert back to grid coordinates

| Value | New Position |
| ----: | -----------: |
|     9 |        (0,0) |
|     1 |        (0,1) |
|     2 |        (0,2) |
|     3 |        (1,0) |
|     4 |        (1,1) |
|     5 |        (1,2) |
|     6 |        (2,0) |
|     7 |        (2,1) |
|     8 |        (2,2) |

Final grid:

```text
[
 [9,1,2],
 [3,4,5],
 [6,7,8]
]
```

---

## Complexity Analysis

Let **m** be the number of rows and **n** be the number of columns.

- **Time Complexity:** `O(m × n)`
  - Every element is processed exactly once.

- **Space Complexity:** `O(m × n)`
  - A new grid of the same size is created to store the shifted result.
