class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0 : 1}
        curSum = res = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefix_map.get(diff, 0)
            prefix_map[curSum] = prefix_map.get(curSum, 0) + 1
        return res