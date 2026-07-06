class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        res = []

        def dfs(i, cur, target):
            if target == 0:
                res.append(cur.copy())
                return
            if i == N or target < 0:
                return
            
            for j in range(i, N):
                if target < 0:
                    return
                cur.append(nums[j])
                dfs(j, cur, target - nums[j])
                cur.pop()
            
        dfs(0, [], target)
        return res