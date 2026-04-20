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
        max_val = max(interval[0] for interval in intervals)

        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1
                    
        if interval_start != -1:
            res.append([interval_start, have])

        return res