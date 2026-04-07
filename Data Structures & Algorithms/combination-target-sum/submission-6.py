class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, target, curList):
            if target < 0 or index >= len(nums):
                return
            elif target == 0:
                res.append(curList.copy())
                return

            dfs(index + 1, target, curList)
            curList.append(nums[index])
            dfs(index, target - nums[index], curList)
            curList.pop()

        dfs(0, target, [])
        return res


'''
dfs
if target reaches negative, return
if target reaches 0, append current list to the result list, return
2, 5, 6, 9
2, 2
2, 5,
add current val to list, i
not add current val, i + 1
'''