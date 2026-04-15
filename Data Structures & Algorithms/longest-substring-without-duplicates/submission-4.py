class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = [0] * 128
        l = longest = 0
        for r in range(len(s)):
            while cnt[ord(s[r])] > 0:
                cnt[ord(s[l])] -= 1
                l += 1
            cnt[ord(s[r])] += 1
            longest = max(longest, r - l + 1)
        return longest