# 863. All Nodes Distance K in Binary Tree

**Difficulty:** Medium

**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree, Graph

🔗 **Problem:** https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

---

## Problem Summary

You are given the root of a binary tree, a target node within that tree, and an integer `k`.

The task is to return the values of every node whose shortest distance from the target node is exactly `k`. The distance between two nodes is measured by the number of edges in the shortest path connecting them.

Since movement is allowed both down to children and up to parents, the tree can be viewed as an undirected graph.

---

## Example

### Example 1

**Input:**

```text
root = [3,5,1,6,2,0,8,null,null,7,4]
target = 5
k = 2
```

**Output:**

```text
[7,4,1]
```

**Explanation:**

Starting from node `5`, the nodes exactly two edges away are `7`, `4`, and `1`. These are the only nodes reachable in two steps.

### Example 2

**Input:**

```text
root = [1]
target = 1
k = 3
```

**Output:**

```text
[]
```

**Explanation:**

The tree contains only one node, so there are no nodes three edges away from the target.

---

## Approach

The implemented solution first converts the binary tree into an undirected graph, then performs a breadth-first search starting from the target node.

### Step 1

Handle the special case where `k` is `0`. In this situation, the target node itself is the only valid answer.

```python
if not k:
    return [target.val]
```

### Step 2

Traverse the tree using BFS and build an adjacency list.

For every parent-child relationship, store connections in both directions so traversal can move upward and downward.

### Step 3

Perform another BFS starting from the target node.

A queue stores each node together with its current distance from the target.

A `visited` set prevents revisiting nodes and avoids infinite traversal.

### Step 4

Whenever a node is dequeued:

- If its distance equals `k`, add its value to the result.
- Otherwise, continue exploring all unvisited neighboring nodes.

Once the traversal finishes, return the collected node values.

---

## Walkthrough

Consider:

```text
          3
        /   \
       5     1
      / \   / \
     6   2 0   8
        / \
       7   4
```

Target:

```text
5
```

Distance:

```text
k = 2
```

### Build the graph

Each edge becomes bidirectional.

| Node | Connected To |
| ---- | ------------ |
| 3    | 5, 1         |
| 5    | 3, 6, 2      |
| 1    | 3, 0, 8      |
| 6    | 5            |
| 2    | 5, 7, 4      |
| 7    | 2            |
| 4    | 2            |
| 0    | 1            |
| 8    | 1            |

### BFS from the target

Initial queue:

| Queue  | Visited |
| ------ | ------- |
| (5, 0) | {5}     |

Process `(5, 0)`:

- Visit `3`
- Visit `6`
- Visit `2`

Queue:

| Queue               |
| ------------------- |
| (3,1), (6,1), (2,1) |

Process `(3,1)`:

- Visit `1`

Queue:

| Queue               |
| ------------------- |
| (6,1), (2,1), (1,2) |

Process `(6,1)`:

- No new neighbors.

Process `(2,1)`:

- Visit `7`
- Visit `4`

Queue:

| Queue               |
| ------------------- |
| (1,2), (7,2), (4,2) |

The remaining nodes are all at distance `2`, so their values are collected.

Result:

```text
[1, 7, 4]
```

The order may vary because any ordering is accepted.

---

## Complexity Analysis

Let **n** be the number of nodes in the binary tree.

- **Time Complexity:** `O(n)`
  - Building the graph visits every node once.
  - The BFS from the target also visits each node at most once.

- **Space Complexity:** `O(n)`
  - The adjacency list, queue, and visited set can each store up to all nodes.
