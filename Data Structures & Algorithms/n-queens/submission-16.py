class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        safeCols = [True for _ in range(n)]
        safeDiag = [[0 for _ in range(n)] for _ in range(n)]
        configs = []

        def setDiag(row, col, tf):
            negCol = col
            safeDiag[row][col] += tf

            while row < n:
                if col < n:
                    safeDiag[row][col] += tf
                if negCol >= 0:
                    safeDiag[row][negCol] += tf
                row += 1
                col += 1
                negCol -= 1


        def placeQueens(row, col, numQueens):
            if numQueens == n:
                configs.append(["".join(map(str, row)) for row in board])
                return

            # for row in range(n):
            for col in range(n):
                if safeCols[col] and safeDiag[row][col] <= 0:
                    # print(row, col, safeDiag)

                    board[row][col] = 'Q'
                    safeCols[col] = False
                    setDiag(row, col, 1)

                    placeQueens(row + 1, 0, numQueens + 1)

                    board[row][col] = "."
                    safeCols[col] = True
                    setDiag(row, col, -1)
                    

                
        placeQueens(0, 0, 0)
        return configs