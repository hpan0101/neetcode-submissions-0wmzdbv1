class Solution:
    '''
        
    '''
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            len_s = int(s[i:j])
            start_s = j + 1
            end_s = start_s + len_s
            res.append(s[start_s: end_s])
            i = end_s
        return res