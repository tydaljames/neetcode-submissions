class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxIsland = 0
        board = grid.copy()
        q = deque()

        def dfs(row, col) -> int:
            if (row < 0 or row >= ROWS or 
                col < 0 or col >= COLS or 
                grid[row][col] == 0):
                return 0

            grid[row][col] = 0

            right = dfs(row, col + 1)
            down = dfs(row + 1, col)
            left = dfs(row, col - 1)
            up = dfs(row - 1, col)

            return right + down + left + up + 1


        for row in range(ROWS):
            for col in range(COLS):
                island = dfs(row, col)
                maxIsland = max(island, maxIsland)
        
        return maxIsland
