class Solution:
    '''
    store num and its count to a map
    add map values, and keys to heap
    if heap larger than k, pop
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return []
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        minHeap = []
        for num in freqMap.keys():
            heapq.heappush(minHeap, (freqMap[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res