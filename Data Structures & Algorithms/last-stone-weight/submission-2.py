class Solution:
    '''
    lastWeight
    while heap:
        pick the top two stones, abs(s1 - s2), push to heap
        update heap[0]
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2: return stones[0]
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            diff = abs(s1 - s2)
            if diff != 0:
                heapq.heappush(heap, -diff)

        return -heap[0] if len(heap) == 1 else 0 
        