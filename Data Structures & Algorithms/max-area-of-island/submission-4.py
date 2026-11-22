class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxIsland = 0
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col) -> int:
            # if (row not in range(ROWS) or
            #     col not in range(COLS) or
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or seen[row][col]:
                return 0

            # print(row, col, grid[row][col])

            seen[row][col] = True

            if grid[row][col] == 0:
                return 0

            right = dfs(row, col + 1)
            down = dfs(row + 1, col)
            left = dfs(row, col - 1)
            up = dfs(row - 1, col)

            return right + down + left + up + 1


        for row in range(ROWS):
            for col in range(COLS):
                island = dfs(row, col)
                # print(island, maxIsland)
                maxIsland = max(island, maxIsland)
        
        return maxIsland
