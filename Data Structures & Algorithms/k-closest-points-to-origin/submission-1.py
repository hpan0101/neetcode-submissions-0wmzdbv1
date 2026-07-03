class Solution:
    '''
    maxheap 
    return k closest point

    maxHeap,
    calculate dis btw p1, p2 (p2 - p1)
    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (-self.calcDist(point), point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]

    def calcDist(self, point: List[int]) -> int:
        return point[1] * point[1] + point[0] * point[0] 