class Solution:
    '''
    search [1, max(piles)]
    l = 1, r = max(piles)
    while l <= r
        mid = l + (r - l) // 2
        total_time = 0
        compute total_time, totaltime = bananas / speed
        if totaltime <= r:
            record mid save to k
            r = mid - 1
        else l = mid + 1
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            mid = l + (r - l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / mid)
            if total_time <= h:
                k = mid
                r = mid - 1
            else: 
                l = mid + 1

        return k