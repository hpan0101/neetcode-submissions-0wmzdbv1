class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        q = deque([(0, 0)])
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        m, n = len(grid), len(grid[0])
        grid[0][0] = 1
        
        dist = 1

        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()
                if r == m - 1 and c == n - 1:
                    return dist
                for dr, dc in DIRS:
                    newR, newC = r + dr, c + dc
                    if newR >= 0 and newC >= 0 and newR < m and newC < n and grid[newR][newC] == 0:
                        q.append((newR, newC))
                        grid[newR][newC] = 1
            dist += 1
        return -1