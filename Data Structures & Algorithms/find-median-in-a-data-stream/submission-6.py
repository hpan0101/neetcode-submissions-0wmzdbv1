class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap
    
    '''

    '''
    def addNum(self, num: int) -> None:
        if not self.large or num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -(heapq.heappop(self.large)))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -(heapq.heappop(self.small)))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return (self.large[0] - self.small[0]) / 2.0