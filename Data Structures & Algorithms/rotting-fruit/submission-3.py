class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh = 0

        def bfs():
            nonlocal fresh
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
                fresh -= 1

                grid[row][col] = -1

                q.append((row, col + 1, time + 1))
                q.append((row + 1, col, time + 1))
                q.append((row, col - 1, time + 1))
                q.append((row - 1, col, time + 1))

            print(fresh)
            return time



        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
                    fresh += 1
                elif grid[row][col] == 1:
                    fresh += 1
        time = bfs()

        return time if fresh == 0 else -1
