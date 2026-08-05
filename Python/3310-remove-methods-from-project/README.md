# 3310. Remove Methods From Project

**Difficulty:** Medium

**Topics:** Graph, Depth-First Search

🔗 **Problem:** https://leetcode.com/problems/remove-methods-from-project/

---

## Problem Summary

You are given a project containing `n` methods and a list of method invocations.

A bug is known to exist in method `k`. Any method that can be reached from `k` through direct or indirect invocations is also considered **suspicious**.

The suspicious methods can only be removed if **no non-suspicious method invokes any suspicious method**. If such an invocation exists, no methods can be removed.

Return the list of methods that remain after removing the suspicious ones. If removal is not possible, return all methods.

---

## Example

### Example 1

**Input:**

```text
n = 4
k = 1
invocations = [[1,2],[0,1],[3,2]]
```

**Output:**

```text
[0,1,2,3]
```

**Explanation:**

Methods `1` and `2` are suspicious, but they are invoked by methods `0` and `3`, which are not suspicious. Therefore, the suspicious methods cannot be removed.

### Example 2

**Input:**

```text
n = 5
k = 0
invocations = [[1,2],[0,2],[0,1],[3,4]]
```

**Output:**

```text
[3,4]
```

**Explanation:**

Methods `0`, `1`, and `2` are suspicious, and no non-suspicious method invokes them. They can be removed, leaving methods `3` and `4`.

### Example 3

**Input:**

```text
n = 3
k = 2
invocations = [[1,2],[0,1],[2,0]]
```

**Output:**

```text
[]
```

**Explanation:**

Starting from method `2`, every method becomes suspicious, so the entire project can be removed.

---

## Approach

The implemented solution first identifies every suspicious method using Depth-First Search (DFS), then verifies whether removing them is allowed.

### Step 1

Build an adjacency list representing the invocation graph.

```python
graph = [[] for _ in range(n)]
```

Each directed edge represents one method invoking another.

### Step 2

Run a DFS starting from the buggy method.

```python
dfs(k)
```

Every reachable method is marked as suspicious.

### Step 3

Check every invocation in the project.

```python
for u, v in invocations:
```

If a non-suspicious method invokes a suspicious one:

```python
if not suspicious[u] and suspicious[v]:
```

then removing the suspicious methods would violate the problem's condition.

Return every method unchanged.

```python
return list(range(n))
```

### Step 4

If no invalid invocation exists, remove all suspicious methods.

```python
return [i for i in range(n) if not suspicious[i]]
```

---

## Walkthrough

Consider:

```text
n = 5
k = 0

invocations =
[
 [1,2],
 [0,2],
 [0,1],
 [3,4]
]
```

### Build the graph

```text
0 → 2
0 → 1
1 → 2
3 → 4
```

### DFS from method 0

Visited methods:

```text
0 → 2
 \
  → 1
```

Suspicious methods:

```text
{0,1,2}
```

Remaining methods:

```text
{3,4}
```

### Validate removability

Check every invocation:

| Invocation | Valid? |
| ---------- | :----: |
| 1 → 2      |   ✓    |
| 0 → 2      |   ✓    |
| 0 → 1      |   ✓    |
| 3 → 4      |   ✓    |

No non-suspicious method calls a suspicious one.

Therefore, the suspicious methods can be removed.

Final result:

```text
[3,4]
```

---

## Complexity Analysis

Let:

- **n** be the number of methods.
- **m** be the number of invocations.

- **Time Complexity:** `O(n + m)`
  - Building the graph, performing DFS, and validating the invocations each require linear time.

- **Space Complexity:** `O(n + m)`
  - The adjacency list, recursion stack, and `suspicious` array require linear additional space.
