# 1406. Stone Game III

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Game Theory

🔗 **Problem:** https://leetcode.com/problems/stone-game-iii/

---

## Problem Summary

Alice and Bob play a game with a row of stones, where each stone has an associated integer value.

Starting with Alice, the players take turns removing **1, 2, or 3** stones from the beginning of the remaining row. Each player adds the values of the stones they take to their score.

Both players always play optimally.

Return:

- `"Alice"` if Alice finishes with a higher score,
- `"Bob"` if Bob finishes with a higher score,
- `"Tie"` if both players end with the same score.

---

## Example

### Example 1

**Input:**

```text
stoneValue = [1,2,3,7]
```

**Output:**

```text
"Bob"
```

**Explanation:**

No matter how Alice starts, Bob can always respond optimally and finish with a higher total score.

### Example 2

**Input:**

```text
stoneValue = [1,2,3,-9]
```

**Output:**

```text
"Alice"
```

**Explanation:**

Alice's optimal strategy is to take the first three stones, leaving the negative-valued stone for Bob and securing a higher final score.

### Example 3

**Input:**

```text
stoneValue = [1,2,3,6]
```

**Output:**

```text
"Tie"
```

**Explanation:**

With optimal play from both sides, neither player can obtain a higher score than the other.

---

## Approach

The implemented solution uses bottom-up dynamic programming.

Instead of storing the players' individual scores, `dp[i]` represents the **maximum score difference** the current player can achieve over the opponent starting from index `i`.

### Step 1

Create a DP array.

```python
dp = [0] * (n + 1)
```

The extra position represents the state where no stones remain.

### Step 2

Process the array from right to left.

For every starting position, evaluate taking:

- 1 stone,
- 2 stones,
- 3 stones.

### Step 3

Maintain the running sum of the stones taken.

```python
total += stoneValue[i + k]
```

### Step 4

Compute the resulting score difference.

After taking the current stones, the opponent will achieve `dp[i + k + 1]`.

Therefore, the current player's advantage becomes:

```python
total - dp[i + k + 1]
```

Choose the move that maximizes this value.

```python
best = max(best, total - dp[i + k + 1])
```

Store the result.

```python
dp[i] = best
```

### Step 5

The value `dp[0]` represents the final score difference.

- If `dp[0] > 0`, Alice wins.
- If `dp[0] < 0`, Bob wins.
- Otherwise, the game ends in a tie.

---

## Walkthrough

Consider:

```text
stoneValue = [1,2,3,7]
```

Build the DP array from right to left.

### Index 3

Remaining stones:

```text
[7]
```

Possible move:

```text
Take 7
```

```text
dp[3] = 7
```

---

### Index 2

Remaining stones:

```text
[3,7]
```

Options:

| Stones Taken | Score Difference |
| ------------ | ---------------: |
| 3            |   3 - dp[3] = -4 |
| 3 + 7        |  10 - dp[4] = 10 |

Best choice:

```text
dp[2] = 10
```

---

### Index 1

Remaining stones:

```text
[2,3,7]
```

Options:

| Stones Taken | Score Difference |
| ------------ | ---------------: |
| 2            |   2 - dp[2] = -8 |
| 2 + 3        |   5 - dp[3] = -2 |
| 2 + 3 + 7    |  12 - dp[4] = 12 |

Best choice:

```text
dp[1] = 12
```

---

### Index 0

Remaining stones:

```text
[1,2,3,7]
```

Options:

| Stones Taken | Score Difference |
| ------------ | ---------------: |
| 1            |  1 - dp[1] = -11 |
| 1 + 2        |   3 - dp[2] = -7 |
| 1 + 2 + 3    |   6 - dp[3] = -1 |

Best result:

```text
dp[0] = -1
```

Since:

```text
dp[0] < 0
```

Bob wins.

---

## Complexity Analysis

Let **n** be the number of stones.

- **Time Complexity:** `O(n)`
  - Each position considers at most three possible moves.

- **Space Complexity:** `O(n)`
  - The DP array stores one value for every starting position.
