class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        safeRows = [True for _ in range(n)]
        safeCols = [True for _ in range(n)]
        safeDiag = [[0 for _ in range(n)] for _ in range(n)]
        # config = board.copy()
        configs = []

        # ['Q', '.', '.', '.', '.', '.'], 
        # ['.', '.', 'Q', '.', '.', '.'], 
        # ['.', '.', '.', '.', '.', 'Q'],
        # ['.', '.', '.', 'Q', '.', '.'], 
        # ['.', 'Q', '.', '.', '.', '.'], 
        # ['.', '.', '.', '.', 'Q', '.']]

        def setDiag(row, col, tf):
            negCol = col
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
                board2 = ["".join(map(str, row)) for row in board]
                # print("~~~~~~")
                # print(board)
                # print(board2)
                # print("~~~~~~")

                configs.append(board2)
                return

            # for row in range(n):
            for col in range(n):
                if safeRows[row] and safeCols[col] and safeDiag[row][col] <= 0:
                    # print(row, col, safeDiag)

                    board[row][col] = 'Q'
                    safeRows[row] = False
                    safeCols[col] = False
                    setDiag(row, col, 1)


                    placeQueens(row + 1, 0, numQueens + 1)

                    board[row][col] = "."
                    safeRows[row] = True
                    safeCols[col] = True
                    setDiag(row, col, -1)
                    

                
        placeQueens(0, 0, 0)
        return configs