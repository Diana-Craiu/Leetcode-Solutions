class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        total = rows * cols
        k %= total

        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                index= i * cols + j

                new_index = (index + k) % total

                new_row = new_index // cols
                new_col = new_index % cols

                result[new_row][new_col] = grid[i][j]

        return result
        