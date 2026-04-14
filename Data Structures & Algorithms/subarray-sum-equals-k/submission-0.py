class Solution:
    '''
    2, -1, 1, 2      k = 2
    cursum = 2           diff = 0
    res = 2
    prefixSums, prefix as key, cnt of prefix as value
        0 : 1
        2 : 2
        1 : 1

    for each num in the array:
        add to curSum
        diff = curSum - k
        add 

    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = {0 : 1}
        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = (1 + prefixSums.get(curSum, 0))
        return res