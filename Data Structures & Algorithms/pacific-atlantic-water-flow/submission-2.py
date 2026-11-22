class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        pac = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atl = [[False for _ in range(COLS)] for _ in range(ROWS)]
        both = [[False for _ in range(COLS)] for _ in range(ROWS)]
        res = []

        def dfs(row, col, prev):
            # print("Iter on", row, col)
            if row < 0 or col < 0:
                return True, False
            if row >= ROWS or col >= COLS:
                return False, True
            if (seen[row][col] or heights[row][col] > prev):
                return False, False
            if both[row][col]:
                return True, True
                
            seen[row][col] = True
            
            left = dfs(row, col - 1, heights[row][col])
            up = dfs(row - 1, col, heights[row][col])
            right = dfs(row, col + 1, heights[row][col])

            # print("going down", ROWS)
            down = dfs(row + 1, col, heights[row][col])
            

            pac[row][col] = pac[row][col] or right[0] or down[0] or left[0] or up[0]
            atl[row][col] = atl[row][col] or right[1] or down[1] or left[1] or up[1]


            # if pac[row][col] and atl[row][col]:
            #     both[row][col] = True

            # print(row, col, left, up, right, down, pac[row][col], atl[row][col], both[row][col])
            

            return (pac[row][col], atl[row][col])


        for row in range(ROWS):
            for col in range(COLS):
                seen = [[False for _ in range(COLS)] for _ in range(ROWS)]

                # print("starting", row, col)
                if dfs(row, col, float('inf')) == (True, True):
                    res.append([row, col])

        # print(res)
        return res