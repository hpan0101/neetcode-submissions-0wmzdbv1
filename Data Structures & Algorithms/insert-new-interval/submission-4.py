class Solution:
    '''
    iterate through intervals, try to add new interval to it
    check if new intervals can be inserted, 
    while [old_start, old_end] [new_start, new_end] old_end < new_start,
        i++
    while index in bound, old_start <= new_end,
        add new intervals
    add the rest of the intervals
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        n = len(intervals)
        res = []
        while index < n and intervals[index][1] < newInterval[0]:
            res.append([intervals[index][0], intervals[index][1]])
            index += 1
        while index < n and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1
        res.append(newInterval)
        while index < n:
            res.append(intervals[index])
            index += 1
        return res
