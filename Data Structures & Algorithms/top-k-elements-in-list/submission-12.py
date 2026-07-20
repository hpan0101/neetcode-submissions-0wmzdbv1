class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        cnt = Counter(nums)

        for num in cnt.keys():
            heapq.heappush(heap, (cnt[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res