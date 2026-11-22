class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        badCols = [False for _ in range(n)]
        badLeftDiag = set()
        badRightDiag = set()
        configs = []

        def placeQueens(row, col, numQueens):
            if numQueens == n:
                configs.append(["".join(map(str, row)) for row in board])
                return

            # for row in range(n):
            for col in range(n):
                if not badCols[col] and (row + col) not in badLeftDiag and (row - col) not in badRightDiag:
                    print(row, col)
                    board[row][col] = 'Q'
                    badCols[col] = True
                    badLeftDiag.add(row + col)
                    badRightDiag.add(row - col)

                    placeQueens(row + 1, 0, numQueens + 1)

                    board[row][col] = "."
                    badCols[col] = False
                    badLeftDiag.remove(row + col)
                    badRightDiag.remove(row - col)
                
        placeQueens(0, 0, 0)
        return configs