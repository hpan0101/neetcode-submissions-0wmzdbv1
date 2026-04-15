class Solution:
    '''
    iterate through t:
        store
        increment unique ch 
    
    '''
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        cnt = [0] * 128
        unique = 0
        minLen = float("infinity")
        minStart = -1
        l = 0
        for c in t:
            if cnt[ord(c)] == 0:
                unique += 1
            cnt[ord(c)] += 1

        for r in range(len(s)):
            c = s[r]
            cnt[ord(c)] -= 1
            if cnt[ord(c)] == 0:
                unique -= 1
            while unique == 0:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    minStart = l
                cnt[ord(s[l])] += 1
                if cnt[ord(s[l])] > 0:
                    unique += 1
                l += 1
            
        return s[minStart: minStart + minLen] if minStart != -1 else ""


