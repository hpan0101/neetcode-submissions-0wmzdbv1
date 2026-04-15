class Solution:
    '''
    iterate r [0, n - 1]
        store s[r] to a set
        while current window have repeating chars, remove s[l] from the set, shrink window from left
        update longest r - l + 1
    return longest
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest