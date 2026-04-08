class Solution:
    '''
    1. sort
    2. add first interval to result
    3. iterate through interval from [1:]
        if lastend >= new_start, able to merge, update end
        else append new start and end to result
    return result
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            oldEnd = res[-1][1]
            if oldEnd >= start:
                res[-1][1] = max(end, oldEnd)
            else:
                res.append([start, end])
        return res
