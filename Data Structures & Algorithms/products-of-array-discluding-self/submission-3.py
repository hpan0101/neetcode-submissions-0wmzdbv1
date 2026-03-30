class Solution:
    '''
    left to right
    if i == 0,  = nums[i]
    prodleft[i] = prodleft[i - 1] * nums[i]
        

    right to left
    if i == n - 1 = nums[i]
    prodright[i] = prodright[i + 1] * nums[i]

    iterate i left to right
    if i == 0, = prodright[i + 1]
    if i == n - 1, = prodleft[i - 1]
    res[i] = prodleft[i - 1] * prodright[i + 1]
    ''' 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        prodleft, prodright, res = [1] * n, [1] * n, [1] * n
        for l in range(n):
            if l == 0:
                prodleft[l] = nums[l]
            else:
                prodleft[l] = prodleft[l - 1] * nums[l]
        for r in range(n - 1, -1, -1):
            if r == n - 1:
                prodright[r] = nums[r]
            else:
                prodright[r] = prodright[r + 1] * nums[r]
        

        for i in range(n):
            if i == 0:
                res[i] = prodright[i + 1]
            elif i == n - 1:
                res[i] = prodleft[i - 1]
            else:
                res[i] = prodleft[i - 1] * prodright[i + 1]
        return res