class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = [0] * 26
        longest = 0
        maxCount = 0
        l = 0

        for i in range(len(s)):
            c = s[i]
            cnt[ord(c) - ord('A')] += 1
            maxCount = max(maxCount, cnt[ord(c) - ord('A')])

            while i - l + 1 - maxCount > k:
                cnt[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, i - l + 1)
        return longest