class Solution:
    '''
    goal: letfmost idx that we can reach
    initialize goal = n - 1
    iterate i [n - 2, 0] cuz n - 1 can be reached
        if i + nums[i] >= goal, update goal to be i
    return if goal is eventaull 0
    '''
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        