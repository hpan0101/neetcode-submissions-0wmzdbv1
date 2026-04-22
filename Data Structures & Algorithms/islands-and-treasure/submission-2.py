class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visited = set()

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0

        def addCell(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append([r, c])

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    addCell(dr + r, dc + c)
            dist += 1