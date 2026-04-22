class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshCount = 0
        m = len(grid)
        n = len(grid[0])
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        steps = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        if freshCount == 0: return 0
        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                for dr, dc in DIRS:
                    newR = dr + r
                    newC = dc + c
                    if newR >= 0 and newC >= 0 and newR < m and newC < n:
                        if grid[newR][newC] == 1:
                            grid[newR][newC] = 2
                            q.append([newR, newC])
                            freshCount -= 1
            steps += 1
            if freshCount == 0:
                return steps
        return steps if freshCount == 0 else -1


        