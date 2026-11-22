class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        def bfs():
            time = 0

            while q:
                node = q.popleft()
                row = node[0]
                col = node[1]

                if (row < 0 or row >= ROWS or 
                    col < 0 or col >= COLS or
                    grid[row][col] <= 0):
                    continue

                time = node[2]

                print(row, col, grid[row][col], time)

                grid[row][col] = -1

                q.append((row, col + 1, time + 1))
                q.append((row + 1, col, time + 1))
                q.append((row, col - 1, time + 1))
                q.append((row - 1, col, time + 1))

            return time



        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col, 0))

        time = bfs()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] > 0:
                    return -1
        return time

