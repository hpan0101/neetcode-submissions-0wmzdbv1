class Solution:
    '''
    caculate frequency and store to a heap
    add (frequency, value) to a minheap,
        if len minheap > k, pop heap
    add what's in the heap to the result list and return
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            res.append(heapq.heappop(heap)[1])
        return res