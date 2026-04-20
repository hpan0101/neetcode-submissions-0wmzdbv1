class Solution:
    '''
    sort the intevals
    add first interval to the result list
    iterate through intervals [1, n - 1]
        if cur_start < last_element_end, update max end
        else, add current interval to the list
    return result list
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last = res[-1]
            if start <= last[1]:
                res[-1][1] = max(last[1], end)
            else:
                res.append([start, end])
        return res 

        