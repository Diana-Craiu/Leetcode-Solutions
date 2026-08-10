# 1510. Stone Game IV

**Difficulty:** Hard

**Topics:** Math, Dynamic Programming, Game Theory

🔗 **Problem:** https://leetcode.com/problems/stone-game-iv/

---

## Problem Summary

Alice and Bob play a game starting with `n` stones.

On each turn, a player must remove a positive perfect square number of stones. A player who cannot make a valid move loses.

Both players play optimally. Return `true` if Alice can force a win, otherwise return `false`.

---

## Example

### Example 1

**Input:**

```text
n = 1
```

**Output:**

```text
true
```

**Explanation:**

Alice can remove one stone because `1` is a perfect square. No stones remain for Bob, so Alice wins.

### Example 2

**Input:**

```text
n = 2
```

**Output:**

```text
false
```

**Explanation:**

Alice can only remove one stone:

```text
2 → 1
```

Bob can then remove the remaining stone:

```text
1 → 0
```

Alice therefore loses.

### Example 3

**Input:**

```text
n = 4
```

**Output:**

```text
true
```

**Explanation:**

Alice can remove all four stones immediately because `4` is a perfect square:

```text
4 → 0
```

Bob has no possible move, so Alice wins.

---

## Approach

The implemented solution uses bottom-up dynamic programming.

`dp[i]` represents whether the player whose turn it is can win when there are exactly `i` stones remaining.

### Step 1

Initialize the DP array.

```python
dp = [False] * (n + 1)
```

By default, every state is considered losing until a winning move is found.

### Step 2

Process every number of stones from `1` to `n`.

```python
for i in range(1, n + 1):
```

For each state, the solution tries every possible square number that can be removed.

### Step 3

Start checking perfect squares from `1`.

```python
square = 1

while square * square <= i:
```

Only square numbers that do not exceed the current number of stones can be removed.

### Step 4

Check the state after removing the current square.

```python
if not dp[i - square * square]:
```

If the resulting state is losing for the next player, the current player can make that move and force a win.

Therefore:

```python
dp[i] = True
```

The search for this state can then stop.

### Step 5

Return the result for `n`.

```python
return dp[n]
```

If `dp[n]` is `True`, Alice has a winning strategy. Otherwise, Bob can force a win.

---

## Walkthrough

Consider:

```text
n = 4
```

### State `1`

The available square is:

```text
1
```

Removing it gives:

```text
1 → 0
```

`dp[0]` is `False`, meaning the next player cannot move.

Therefore:

```text
dp[1] = True
```

### State `2`

The only possible square is `1`.

After removing it:

```text
2 → 1
```

But:

```text
dp[1] = True
```

so the next player has a winning position.

There is no other valid move.

Therefore:

```text
dp[2] = False
```

### State `3`

Possible square:

```text
1
```

After removing it:

```text
3 → 2
```

Since:

```text
dp[2] = False
```

the current player can force a win.

Therefore:

```text
dp[3] = True
```

### State `4`

Possible squares include:

```text
1
4
```

Taking `4` gives:

```text
4 → 0
```

Since:

```text
dp[0] = False
```

Alice can win immediately.

Therefore:

```text
dp[4] = True
```

The algorithm returns:

```text
true
```

---

## Complexity Analysis

Let **n** be the number of stones.

- **Time Complexity:** `O(n√n)`
  - For each value from `1` to `n`, the solution checks all possible square numbers up to that value.

- **Space Complexity:** `O(n)`
  - The DP array stores one boolean value for every possible number of remaining stones.
