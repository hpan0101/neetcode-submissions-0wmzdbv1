class Solution:
    '''
    maxheap 
    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points: return []
        heap = []
        for point in points:
            distance = self.calcDis(point[0], point[1])
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
    
    def calcDis(self, x: int, y: int) -> int:
        return math.sqrt((x - 0) ** 2 + (y - 0) ** 2)