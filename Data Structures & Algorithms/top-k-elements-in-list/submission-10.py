class Solution:
    '''
    num to key 
    minheap k = 2 [1, 2, 2, 3, 3]
     3, 3   3 nlogk
    
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        heap = []
        for num in cnt.keys():
            heapq.heappush(heap, (cnt[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res