class Solution:
    '''
    sort the nums
    iterate through the array to find the first num:
        if a > 0 continue
        else, find the rest of the 2 pointers l = i + 1, r = n - 1
            if nums[l] + nums[r] - a < 0:
                l++
            else if nums[l] + nums[r] - a > 0:
                r--
            else:
                dedup
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        res = []
        n = len(nums)
        for i, a in enumerate(nums):
            if a > 0: continue
            l = i + 1
            r = n - 1
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            while l < r:
                threeSum = nums[l] + nums[r] + a
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        
        return res
        
