class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col, i):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or seen[row][col] or board[row][col] != word[i]:
                return False


            char = word[i]
            i += 1
            if i == len(word):
                return True

            seen[row][col] = True

            tf = dfs(row, col + 1, i) or dfs(row + 1, col, i) or dfs(row, col - 1, i) or dfs(row - 1, col, i)

            seen[row][col] = False

            return tf
            
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False
