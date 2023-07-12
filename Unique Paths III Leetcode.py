class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        sr, sc, zeros = [(r, c, sum(1 for row in grid for element in row if element == 0)) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1][0]
        def dfs(r,c,zeros):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1:
                return 0
            if grid[r][c] == 2:
                return 1 if zeros == -1 else 0
            grid[r][c] = -1
            zeros-=1
            ans = (dfs(r+1,c,zeros) + dfs(r,c+1,zeros) + dfs(r-1,c,zeros) + dfs(r,c-1,zeros))
            grid[r][c] = 0
            zeros+=1
            return ans
        return dfs(sr,sc,zeros)
