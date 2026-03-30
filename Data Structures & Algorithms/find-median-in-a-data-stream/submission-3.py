class MedianFinder:
    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        while len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

        while len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return float(self.large[0])

        
        