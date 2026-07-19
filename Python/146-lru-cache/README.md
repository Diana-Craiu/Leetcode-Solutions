# 146. LRU Cache

**Difficulty:** Medium

**Topics:** Hash Table, Linked List, Design, Doubly-Linked List

🔗 **Problem:** https://leetcode.com/problems/lru-cache/

---

## Problem Summary

Design a data structure that implements a **Least Recently Used (LRU) Cache** with a fixed capacity.

The cache should support two operations:

- `get(key)` – Return the value associated with the key if it exists; otherwise return `-1`. Accessing a key marks it as the most recently used.
- `put(key, value)` – Insert or update a key-value pair. If adding a new key exceeds the cache's capacity, remove the least recently used entry before inserting the new one.

Both operations must run in **O(1)** average time.

---

## Example

### Example 1

**Input:**

```text
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]

[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
```

**Output:**

```text
[null, null, null, 1, null, -1, null, -1, 3, 4]
```

**Explanation:**

- Create an LRU cache with capacity `2`.
- Insert `(1,1)` and `(2,2)`.
- Access key `1`, making it the most recently used.
- Insert `(3,3)`, which removes key `2` because it is now the least recently used.
- Accessing key `2` returns `-1`.
- Insert `(4,4)`, which removes key `1`.
- The remaining keys are `3` and `4`, so subsequent lookups return `3` and `4`.

---

## Approach

The implemented solution uses Python's `OrderedDict` to maintain the order in which keys are used.

### Step 1

Initialize the cache with:

- the maximum capacity,
- an `OrderedDict` that stores key-value pairs while preserving their usage order.

```python
self.capacity = capacity
self.keys = OrderedDict()
```

### Step 2

Implement `get()`.

- If the key does not exist, return `-1`.
- Otherwise, move the key to the end of the `OrderedDict` to mark it as the most recently used.
- Return its stored value.

### Step 3

Implement `put()` for existing keys.

- Update the value.
- Move the key to the end so it becomes the most recently used entry.

### Step 4

When inserting a new key:

- If the cache has reached its capacity, remove the first item in the `OrderedDict`, which represents the least recently used key.

```python
self.keys.popitem(last=False)
```

### Step 5

Insert the new key-value pair and move it to the end to mark it as the most recently used.

---

## Walkthrough

Assume the cache capacity is:

```text
2
```

### Put(1, 1)

Cache:

|     Order | Cache |
| --------: | ----- |
| LRU → MRU | {1=1} |

### Put(2, 2)

Cache:

|     Order | Cache      |
| --------: | ---------- |
| LRU → MRU | {1=1, 2=2} |

### Get(1)

Key `1` is accessed and becomes the most recently used.

Cache:

|     Order | Cache      |
| --------: | ---------- |
| LRU → MRU | {2=2, 1=1} |

Returned value:

```text
1
```

### Put(3, 3)

The cache is full.

The least recently used key is `2`, so it is removed.

Cache:

|     Order | Cache      |
| --------: | ---------- |
| LRU → MRU | {1=1, 3=3} |

### Get(2)

Key `2` no longer exists.

Returned value:

```text
-1
```

### Put(4, 4)

Again, the cache is full.

The least recently used key is now `1`, so it is removed.

Cache:

|     Order | Cache      |
| --------: | ---------- |
| LRU → MRU | {3=3, 4=4} |

Subsequent operations return:

```text
get(1) → -1
get(3) → 3
get(4) → 4
```

---

## Complexity Analysis

Let **n** be the maximum cache capacity.

- **Time Complexity:** `O(1)` average for both `get()` and `put()`
  - `OrderedDict` supports lookup, insertion, deletion, and moving elements to the end in constant average time.

- **Space Complexity:** `O(n)`
  - The cache stores at most `capacity` key-value pairs.
