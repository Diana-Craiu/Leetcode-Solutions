# 877. Stone Game

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Game Theory, Recursion, Memoization

🔗 **Problem:** https://leetcode.com/problems/stone-game/

---

## Problem Summary

Alice and Bob play a game with an even number of stone piles arranged in a row.

On each turn, a player removes the entire pile from either the beginning or the end of the row, adding its stones to their score. Both players always make optimal decisions.

The total number of stones is odd, so a tie is impossible.

Return `true` if Alice can finish with more stones than Bob; otherwise, return `false`.

---

## Example

### Example 1

**Input:**

```text
piles = [5,3,4,5]
```

**Output:**

```text
true
```

**Explanation:**

Alice can choose either end pile, both containing `5` stones. Regardless of Bob's response, Alice can continue making optimal choices and finish with more stones than Bob.

### Example 2

**Input:**

```text
piles = [3,7,2,3]
```

**Output:**

```text
true
```

**Explanation:**

By playing optimally, Alice can always secure a higher total number of stones than Bob.

---

## Approach

The implemented solution uses recursive dynamic programming with memoization.

Instead of tracking the players' individual scores, it computes the **maximum score difference** the current player can achieve over the opponent for every subarray of piles.

### Step 1

Create a memoized recursive function.

```python
@cache
def dp(left, right):
```

The function returns the maximum score difference the current player can guarantee using the piles between `left` and `right`.

### Step 2

Handle the base case.

If only one pile remains, the current player takes it.

```python
if left == right:
    return piles[left]
```

### Step 3

Evaluate both possible moves.

Take the left pile:

```python
take_left = piles[left] - dp(left + 1, right)
```

Take the right pile:

```python
take_right = piles[right] - dp(left, right - 1)
```

The recursive call represents the opponent's best achievable score difference, so it is subtracted from the value of the chosen pile.

### Step 4

Choose the move that maximizes the current player's advantage.

```python
return max(take_left, take_right)
```

### Step 5

Evaluate the entire array.

If the resulting score difference is positive, Alice finishes with more stones than Bob.

```python
return dp(0, n - 1) > 0
```

---

## Walkthrough

Consider:

```text
piles = [5,3,4,5]
```

### Initial call

```text
dp(0,3)
```

Alice has two choices.

### Choose the left pile

Take:

```text
5
```

Remaining piles:

```text
[3,4,5]
```

Score difference:

```text
5 - dp(1,3)
```

### Choose the right pile

Take:

```text
5
```

Remaining piles:

```text
[5,3,4]
```

Score difference:

```text
5 - dp(0,2)
```

The recursion evaluates both possibilities while always assuming the opponent also plays optimally.

The larger score difference is stored for each subarray, preventing repeated computations through memoization.

For the complete array:

```text
dp(0,3) > 0
```

Therefore, Alice can guarantee a higher score.

The algorithm returns:

```text
true
```

---

## Complexity Analysis

Let **n** be the number of piles.

- **Time Complexity:** `O(n²)`
  - There are `O(n²)` distinct `(left, right)` states, each computed once.

- **Space Complexity:** `O(n²)`
  - The memoization cache stores one value for each subarray, and the recursion depth is at most `O(n)`.
