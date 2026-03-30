class Solution:
    '''
    add all the num to a set
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seq = set(nums)
        longest = 0
        for num in seq:
            cur = 0
            while num in seq:
                num += 1
                cur += 1
            longest = max(longest, cur)
        return longest
