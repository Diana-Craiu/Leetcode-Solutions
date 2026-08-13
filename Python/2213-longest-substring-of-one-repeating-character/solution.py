class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: list[int]
    ) -> list[int]:

        n = len(s)

        # each node:
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def make_node(ch):
            return [ch, ch, 1, 1, 1, 1]

        def merge(left, right):
            left_char, left_right, left_prefix, left_suffix, left_best, left_len = left
            right_left, right_char, right_prefix, right_suffix, right_best, right_len = right

            prefix = left_prefix
            suffix = right_suffix

            # Entire left interval can be attached to prefix
            if left_prefix == left_len and left_right == right_left:
                prefix = left_len + right_prefix

            # Entire right interval can be attached to suffix
            if right_suffix == right_len and left_right == right_left:
                suffix = right_len + left_suffix

            # Best answer can cross the boundary
            best = max(
                left_best,
                right_best,
                left_suffix + right_prefix
                if left_right == right_left
                else 0
            )

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                left_len + right_len
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = make_node(s[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = make_node(ch)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans