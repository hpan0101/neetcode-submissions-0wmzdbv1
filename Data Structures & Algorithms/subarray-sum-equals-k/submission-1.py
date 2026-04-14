class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0 : 1}
        curSum = res = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in prefix_map:
                res += prefix_map[diff]
            prefix_map[curSum] = prefix_map.get(curSum, 0) + 1
        return res