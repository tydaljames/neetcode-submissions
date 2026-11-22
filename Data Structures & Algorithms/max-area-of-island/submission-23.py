class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxIsland = 0
        q = deque()

        def bfs(row, col):         
            q.appendleft((row, col))
            island = 0

            while(q):
                node = q.pop()
                row = node[0]
                col = node[1]
                if (row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or
                    grid[row][col] == 0):
                    continue

                grid[row][col] = 0
                island += 1

                if col + 1 < COLS:
                    q.appendleft((row, col + 1))
                if row + 1 < ROWS:
                    q.appendleft((row + 1, col))
                if col - 1 >= 0:
                    q.appendleft((row, col - 1))
                if row - 1 >= 0:
                    q.appendleft((row - 1, col))
                
            return island


        # def dfs(row, col) -> int:
        #     if (row < 0 or row >= ROWS or 
        #         col < 0 or col >= COLS or 
        #         grid[row][col] == 0):
        #         return 0

        #     grid[row][col] = 0

        #     right = dfs(row, col + 1)
        #     down = dfs(row + 1, col)
        #     left = dfs(row, col - 1)
        #     up = dfs(row - 1, col)

        #     return right + down + left + up + 1


        for row in range(ROWS):
            for col in range(COLS):
                island = bfs(row, col)
                maxIsland = max(island, maxIsland)
        
        return maxIsland
