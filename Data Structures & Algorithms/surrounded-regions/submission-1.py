class Solution:
    def solve(self, board: List[List[str]]) -> None: 
        q = deque()
        M, N = len(board), len(board[0])
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(M):
            for c in range(N):
                if (r == 0 or c == 0 or r == M - 1 or c == N - 1) and board[r][c] == 'O':
                    q.append([r, c])
        
        while q:
            r, c = q.popleft()
            if board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in DIRS:
                    newR = dr + r
                    newC = dc + c
                    if newR >= 0 and newC >= 0 and newR < M and newC < N:
                        q.append((newR, newC))

        for r in range(M):
            for c in range(N):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

