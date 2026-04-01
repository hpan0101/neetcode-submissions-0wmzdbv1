class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        input_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        res = []

        def dfs(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return
            
            char_candidates = input_map[digits[i]]
            for c in char_candidates:
                dfs(i + 1, curStr + c)
        
        dfs(0, '')
        return res