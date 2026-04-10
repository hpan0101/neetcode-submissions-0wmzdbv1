class Solution:
    '''
    use dfs to track all the possibility, if word is found, return true
    base: if outbound bound, or current char doesn't match word, return false
    recursion
    expand four dirs check if any of them return true, mark char to some other number if visited

    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, word_i):
            if word_i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == '#' or board[r][c] != word[word_i]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            res = False
            for dr, dc in DIRS:
                if dfs(dr + r, dc + c, word_i + 1):
                    res = True
                    break
            board[r][c] = temp
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if (dfs(r, c, 0)):
                    return True
        return False
