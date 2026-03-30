class Solution:
    '''
        add len(str) + '#' + str to the result str
    '''
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    '''
        while i in range
            have j to find the next '#' start from i
            once found, s[i, j] is length
            current str is s[j + 1, j + 1 + len]
            move i = j + 1 + len
        return result list
    '''
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res