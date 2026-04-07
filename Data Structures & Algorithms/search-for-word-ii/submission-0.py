class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0
    
    def addWord(self, word, idx):
        cur = self
        cur.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1
        cur.idx = idx


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def getIndex(c):
            index = ord(c) - ord('a')
            return index

        def dfs(r, c, node):
            idx = getIndex(board[r][c])
            if not node.children[idx]:
                return
            
            tmp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[idx]
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                # Simple node removal optimization logic needs careful handling
                # Removing refs/pruning to keep user structure but fixing typos
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '*':
                    dfs(nr, nc, node)

            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return res