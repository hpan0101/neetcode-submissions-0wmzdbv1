class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                cur = 0
                while num in numSet:
                    num += 1
                    cur += 1
                longest = max(longest, cur)
        return longest