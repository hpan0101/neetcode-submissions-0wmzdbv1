class Solution:
    '''
    have an empty list ready
    for each str in the strs:
        initialize a 26 one d array with zeros
        iterate through its characters:
            increate count of corresponding array
            convert the array to tuple and use it as key
            append the string to the group
        after processing all strs, return all the lists stored in the haspmap



    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            
            res[tuple(cnt)].append(s)
        return list(res.values())