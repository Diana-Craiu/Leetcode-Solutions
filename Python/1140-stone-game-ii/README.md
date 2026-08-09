# 1140. Stone Game II

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Game Theory, Memoization

🔗 **Problem:** https://leetcode.com/problems/stone-game-ii/

---

## Problem Summary

Alice and Bob play a game with piles of stones arranged in a row.

On each turn, the current player can take the first `X` remaining piles, where `X` can be any value from `1` to `2 * M`. After taking the piles, `M` becomes `max(M, X)`. Initially, `M = 1`.

Both players play optimally. Return the maximum number of stones Alice can collect by the end of the game.

---

## Example

### Example 1

**Input:**

```text
piles = [2,7,9,4,4]
```

**Output:**

```text
10
```

**Explanation:**

Alice can start by taking the first pile containing `2` stones. Bob can then take two piles, leaving Alice with the final two piles.

Alice's total is:

```text
2 + 4 + 4 = 10
```

This is better than the result Alice can obtain by taking two piles initially.

### Example 2

**Input:**

```text
piles = [1,2,3,4,5,100]
```

**Output:**

```text
104
```

**Explanation:**

With optimal choices from both players, Alice can guarantee a total of `104` stones.

---

## Approach

The implemented solution uses suffix sums and recursive dynamic programming with memoization.

The state is represented by the current pile index `i` and the current value of `M`.

### Step 1

Build a suffix-sum array.

```python
suffix = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    suffix[i] = suffix[i + 1] + piles[i]
```

`suffix[i]` represents the total number of stones in all piles from index `i` to the end.

This allows the total number of remaining stones to be obtained directly.

### Step 2

Define the memoized dynamic programming function.

```python
@lru_cache(None)
def dp(i, M):
```

The state represents the maximum number of stones the current player can obtain starting at pile `i` with the current limit `M`.

### Step 3

Handle the case where the current player can take all remaining piles.

```python
if i + 2 * M >= n:
    return suffix[i]
```

If the player is allowed to take all remaining piles, they collect the entire suffix.

### Step 4

Try every possible number of piles to take.

```python
for X in range(1, 2 * M + 1):
```

After taking `X` piles, the next state has:

```python
new_M = max(M, X)
```

### Step 5

Calculate the stones the current player can secure.

The total remaining stones are:

```python
suffix[i]
```

The opponent can obtain:

```python
dp(i + X, new_M)
```

Therefore, the current player's resulting amount is:

```python
current = suffix[i] - dp(i + X, new_M)
```

The best possible choice is stored in `best`.

### Step 6

Start the game from the first pile with `M = 1`.

```python
return dp(0, 1)
```

---

## Walkthrough

Consider:

```text
piles = [2,7,9,4,4]
```

The suffix sums are:

```text
index:   0   1   2   3   4
suffix: 26  24  17   8   4
```

Initially:

```text
i = 0
M = 1
```

Alice can take between:

```text
1 and 2
```

piles.

### Take 1 pile

Alice gets:

```text
2
```

The new state becomes:

```text
i = 1
M = 1
```

Bob then chooses optimally from the remaining piles.

The DP calculates the number of stones Bob can obtain from this state and subtracts it from the total remaining stones.

### Take 2 piles

Alice gets:

```text
2 + 7 = 9
```

The new state becomes:

```text
i = 2
M = 2
```

Bob can now take up to four piles and can potentially take everything remaining.

The recursive state evaluation determines Alice's resulting total.

### Choose the better result

The DP compares all possible choices and ultimately determines that the best strategy gives Alice:

```text
10
```

Therefore, the algorithm returns:

```text
10
```

---

## Complexity Analysis

Let **n** be the number of piles.

- **Time Complexity:** `O(n³)`
  - There are `O(n²)` possible `(i, M)` states, and each state considers up to `O(n)` possible values of `X`.

- **Space Complexity:** `O(n²)`
  - The memoization cache can contain `O(n²)` states, and the suffix-sum array requires `O(n)` additional space.
