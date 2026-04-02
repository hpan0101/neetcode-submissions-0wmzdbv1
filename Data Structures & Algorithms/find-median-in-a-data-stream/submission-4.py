class MedianFinder:
    '''
    store small portion to maxheap
    store large portion to minheap
    '''
    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap
    
    '''
    k largest 
    minheap: 4 5 6 7
    7

    if minheap(large) is empty and num is > minheap, add to minheap
    else add to maxheap(min)

    rebalance

    '''
    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

    '''
    return whichever heap has one more element

    return even number / 2
    '''
    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return float(self.large[0])
        elif len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (self.large[0] + -self.small[0]) / 2.0
        
