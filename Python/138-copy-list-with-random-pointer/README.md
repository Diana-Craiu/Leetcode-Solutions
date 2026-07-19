# 138. Copy List with Random Pointer

**Difficulty:** Medium

**Topics:** Hash Table, Linked List

🔗 **Problem:** https://leetcode.com/problems/copy-list-with-random-pointer/

---

## Problem Summary

Given a linked list where each node contains both a `next` pointer and a `random` pointer, create a deep copy of the entire list.

The copied list must contain entirely new nodes while preserving the same structure of both the `next` and `random` relationships. None of the pointers in the copied list should reference nodes from the original list.

---

## Example

### Example 1

```text
Input:
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]

Output:
[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

Explanation:

The copied list contains the same node values and preserves every `next` and `random` connection, but every node is newly created.

---

### Example 2

```text
Input:
head = [[1,1],[2,1]]

Output:
[[1,1],[2,1]]
```

Explanation:

Both copied nodes preserve their original `random` references while remaining completely independent from the original list.

---

### Example 3

```text
Input:
head = [[3,null],[3,0],[3,null]]

Output:
[[3,null],[3,0],[3,null]]
```

Explanation:

The copied list maintains the same structure of `next` and `random` pointers without sharing any nodes with the original list.

---

## Approach

This solution performs the deep copy in two passes using a dictionary.

### Step 1

Traverse the original linked list and create a new node for every existing node.

Store the mapping between the original node and its copy.

```python
new_nodes[original_node] = copied_node
```

---

### Step 2

Traverse the list a second time.

For each original node:

- assign the `next` pointer of its copied node;
- assign the `random` pointer of its copied node.

Since every copied node has already been created, both pointers can be assigned directly using the dictionary.

---

### Step 3

Return the copied version of the original head node.

---

## Walkthrough

Original list:

```text
7 -> 13 -> 11 -> 10 -> 1
```

Random pointers:

```text
7  -> null
13 -> 7
11 -> 1
10 -> 11
1  -> 7
```

### First Pass

Create a copy of every node.

| Original Node | Copied Node |
| ------------- | ----------- |
| 7             | 7           |
| 13            | 13          |
| 11            | 11          |
| 10            | 10          |
| 1             | 1           |

The dictionary now maps every original node to its corresponding copied node.

---

### Second Pass

Assign the `next` and `random` pointers.

| Copied Node | Next | Random |
| ----------- | ---- | ------ |
| 7           | 13   | null   |
| 13          | 11   | 7      |
| 11          | 10   | 1      |
| 10          | 1    | 11     |
| 1           | null | 7      |

The copied list has the exact same structure as the original while containing only newly created nodes.

---

## Complexity Analysis

Let **n** be the number of nodes in the linked list.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

The algorithm traverses the linked list twice and stores one copied node for each original node.
