class Solution:
    '''
    set 
    iterate through set,
        if smaller num found, skip
        else, start counting and updating the longest

    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                cur = 0
                while num in numSet:
                    cur += 1
                    num += 1
                longest = max(longest, cur)
        return longest
        