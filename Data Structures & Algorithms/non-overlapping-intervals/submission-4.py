class Solution:
    '''
    1. sort the intervals
    2. initiate one d dp array len(intervals) with 0 dp[i] represent max non overlapping to index i
    3. iterate through dp i [0, n - 1]
        j [0, ]

    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return res