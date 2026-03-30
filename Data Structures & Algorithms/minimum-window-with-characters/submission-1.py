class Solution:
    '''
    sliding window
    iterate r [0, n - 1]
        add current s[r] to map
        while current sliding window presents all char in t,
            update shortest s[l: r + 1]
            remove char s[l] from map
            move l++
        
    return shortest
            
            
    '''
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}
        l = 0
        
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        need = len(countT)
        have = 0
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update shortest
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                char_l = s[l]
                window[char_l] -= 1
                if char_l in countT and window[char_l] < countT[char_l]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""