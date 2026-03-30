class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = dict()
        for i, num in enumerate(nums):
            if target - num in prevMap:
                return [prevMap[target - num], i]
            prevMap[num] = i
