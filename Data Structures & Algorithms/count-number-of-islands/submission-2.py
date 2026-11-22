class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or seen[row][col]:
                return False

            # print(row, col, grid[row][col], seen[row][col])

            seen[row][col] = True

            if grid[row][col] == "0":
                return False

            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)

            # print("found an island")
            return True

        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col):
                    islands += 1
        return islands
