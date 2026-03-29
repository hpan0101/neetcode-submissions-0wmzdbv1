class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
        for num, c in cnt.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res