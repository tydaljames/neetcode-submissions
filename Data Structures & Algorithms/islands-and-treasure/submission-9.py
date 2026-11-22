class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        NO_TREASURE = 2147483646



        def bfs(row, col, q):
            while q:
                node = q.popleft()
                row = node[0]
                col = node[1]
                breadth = node[2]

                if (row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or
                    seen[row][col] or
                    grid[row][col] == -1):
                    continue

                seen[row][col] = True

                grid[row][col] = breadth

                q.append((row, col + 1, breadth + 1))
                q.append((row + 1, col, breadth + 1))
                q.append((row, col - 1, breadth + 1))
                q.append((row - 1, col, breadth + 1))
                
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]
        q = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col, 0))


        bfs(row, col, q)

            # print(grid)

