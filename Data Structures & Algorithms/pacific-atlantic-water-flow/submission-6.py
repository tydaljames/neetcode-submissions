class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        pac = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atl = [[False for _ in range(COLS)] for _ in range(ROWS)]
        both = []

        def dfs(row, col, prev, pacatl):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                pacatl[row][col] or
                heights[row][col] < prev):
                return

            pacatl[row][col] = True

            print(row, col, prev)

            dfs(row, col + 1, heights[row][col], pacatl)
            dfs(row + 1, col, heights[row][col], pacatl)
            dfs(row, col - 1, heights[row][col], pacatl)
            dfs(row - 1, col, heights[row][col], pacatl)


        print("Starting rows")
        for row in range(ROWS):
            dfs(row, 0, float('-inf'), pac)
            dfs(row, COLS - 1, float('-inf'), atl)

        print("Starting cols")
        for col in range(COLS):
            dfs(0, col, float('-inf'), pac)
            dfs(ROWS - 1, col, float('-inf'), atl)

        for row in range(ROWS):
            for col in range(COLS):
                if pac[row][col]:
                    print(row, col, "pac")
                if atl[row][col]:
                    print(row, col, "atl")

                if pac[row][col] and atl[row][col]:
                    both.append([row, col])

        return both