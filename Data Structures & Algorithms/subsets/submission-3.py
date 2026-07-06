class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        def dfs(i, cur):
            if i == N:
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)

        
        dfs(0, [])
        return res