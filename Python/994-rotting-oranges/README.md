# 994. Rotting Oranges

**Difficulty:** Medium

**Topics:** Array, Breadth-First Search, Matrix

🔗 **Problem:** https://leetcode.com/problems/rotting-oranges/

---

## Problem Summary

You are given an `m × n` grid representing a box of oranges.

Each cell can contain:

- `0` — an empty cell,
- `1` — a fresh orange,
- `2` — a rotten orange.

Every minute, any fresh orange that is directly adjacent (up, down, left, or right) to a rotten orange also becomes rotten.

Return the minimum number of minutes required until every fresh orange has rotted. If some fresh oranges can never be reached, return `-1`.

---

## Example

### Example 1

**Input:**

```text
grid = [[2,1,1],[1,1,0],[0,1,1]]
```

**Output:**

```text
4
```

**Explanation:**

The infection spreads outward from the initially rotten orange. After four minutes, every fresh orange has become rotten.

### Example 2

**Input:**

```text
grid = [[2,1,1],[0,1,1],[1,0,1]]
```

**Output:**

```text
-1
```

**Explanation:**

One fresh orange is isolated by empty cells, so it can never become rotten.

### Example 3

**Input:**

```text
grid = [[0,2]]
```

**Output:**

```text
0
```

**Explanation:**

There are no fresh oranges at the beginning, so no time is needed.

---

## Approach

The implemented solution uses a multi-source Breadth-First Search (BFS), where all initially rotten oranges begin spreading the infection simultaneously.

### Step 1

Traverse the grid once to:

- Count the total number of fresh oranges.
- Add the position of every rotten orange to the BFS queue.

### Step 2

Define the four possible movement directions:

- Right
- Left
- Down
- Up

These directions are used to examine neighboring cells.

### Step 3

Perform BFS level by level.

Each level represents one minute. For every rotten orange currently in the queue:

- Check its four neighboring cells.
- If a neighboring cell contains a fresh orange:
  - Mark it as rotten.
  - Add it to the queue.
  - Decrease the fresh orange count.

After processing the entire current level, increment the elapsed time.

### Step 4

Continue until either:

- All fresh oranges have rotted, or
- The queue becomes empty.

Return the elapsed time if every fresh orange has rotted; otherwise return `-1`.

---

## Walkthrough

Consider the following grid:

```text
2 1 1
1 1 0
0 1 1
```

Initial state:

- Fresh oranges = **6**
- Queue = **[(0,0)]**

### Minute 0

Process `(0,0)`.

Newly rotten:

```text
(0,1), (1,0)
```

Grid:

```text
2 2 1
2 1 0
0 1 1
```

Queue:

```text
[(0,1), (1,0)]
```

### Minute 1

Process both oranges.

Newly rotten:

```text
(0,2), (1,1)
```

Grid:

```text
2 2 2
2 2 0
0 1 1
```

Queue:

```text
[(0,2), (1,1)]
```

### Minute 2

Process the next level.

Newly rotten:

```text
(2,1)
```

Grid:

```text
2 2 2
2 2 0
0 2 1
```

Queue:

```text
[(2,1)]
```

### Minute 3

Process `(2,1)`.

Newly rotten:

```text
(2,2)
```

Grid:

```text
2 2 2
2 2 0
0 2 2
```

Queue:

```text
[(2,2)]
```

At this point, every orange is rotten.

Total time:

```text
4 minutes
```

---

## Complexity Analysis

Let **m** be the number of rows and **n** be the number of columns.

- **Time Complexity:** `O(m × n)`
  - The grid is scanned once initially, and each orange is processed at most once during BFS.

- **Space Complexity:** `O(m × n)`
  - In the worst case, the queue may contain a large portion of the oranges simultaneously.
