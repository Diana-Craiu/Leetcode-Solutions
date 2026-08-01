# 486. Predict the Winner

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Recursion, Memoization, Game Theory

🔗 **Problem:** https://leetcode.com/problems/predict-the-winner/

---

## Problem Summary

Two players take turns choosing either the first or the last number from an integer array. Each chosen number is added to the player's score, and both players always play optimally.

Determine whether Player 1 can guarantee a score that is greater than or equal to Player 2's score. If the scores are tied, Player 1 is considered the winner.

---

## Example

### Example 1

**Input:**

```text
nums = [1,5,2]
```

**Output:**

```text
false
```

**Explanation:**

No matter whether Player 1 chooses `1` or `2`, Player 2 can always take `5`, resulting in a higher final score.

### Example 2

**Input:**

```text
nums = [1,5,233,7]
```

**Output:**

```text
true
```

**Explanation:**

Player 1 can force a strategy that allows them to collect `233`, ensuring a score at least as large as Player 2's.

---

## Approach

The implemented solution uses recursive dynamic programming with memoization.

Instead of tracking the individual scores of both players, the recursion computes the **maximum score difference** the current player can achieve over the opponent for every subarray.

### Step 1

Define a memoized recursive function.

```python
@cache
def dfs(left, right):
```

The function returns the maximum score difference the current player can obtain when playing on the subarray `nums[left:right+1]`.

### Step 2

Handle the base case.

If only one number remains, the current player takes it.

```python
if left == right:
    return nums[left]
```

### Step 3

Evaluate both possible moves.

Take the left element:

```python
take_left = nums[left] - dfs(left + 1, right)
```

Take the right element:

```python
take_right = nums[right] - dfs(left, right - 1)
```

The recursive call represents the opponent's best possible score difference, so it is subtracted from the value just taken.

### Step 4

Choose the better option.

```python
return max(take_left, take_right)
```

### Step 5

If the final score difference is non-negative, Player 1 can guarantee at least a tie.

```python
return dfs(0, len(nums) - 1) >= 0
```

---

## Walkthrough

Consider:

```text
nums = [1,5,2]
```

### Initial call

```text
dfs(0,2)
```

Player 1 has two choices.

### Choose the left value

Take:

```text
1
```

Remaining array:

```text
[5,2]
```

Score difference:

```text
1 - dfs(1,2)
```

### Choose the right value

Take:

```text
2
```

Remaining array:

```text
[1,5]
```

Score difference:

```text
2 - dfs(0,1)
```

The recursive function computes the opponent's optimal response for each case and returns the larger score difference.

The final result is:

```text
dfs(0,2) < 0
```

Since the score difference is negative, Player 1 cannot guarantee a tie or a win.

The algorithm returns:

```text
false
```

---

## Complexity Analysis

Let **n** be the length of the array.

- **Time Complexity:** `O(n²)`
  - There are `O(n²)` distinct `(left, right)` states, and each state is computed once due to memoization.

- **Space Complexity:** `O(n²)`
  - The memoization cache stores one value for each subarray, and the recursion depth is at most `O(n)`.
