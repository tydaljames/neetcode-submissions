class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                board[row][col] != "O" or
                seen[row][col]):
                return

            seen[row][col] = True

            dfs(row, col + 1)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row - 1, col)

        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)

        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and not seen[row][col]:
                    board[row][col] = "X"


