class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        cnt = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for di, dj in DIRS:
                dfs(i + di, j + dj)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    cnt += 1
                    dfs(r, c)
        return cnt
