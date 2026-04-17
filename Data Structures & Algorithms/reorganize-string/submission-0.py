class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-cnt, c] for c, cnt in count.items()]
        heapq.heapify(max_heap)
        prev = None
        res = ""

        while max_heap or prev:
            if prev and not max_heap: return ""
            cnt, c = heapq.heappop(max_heap)
            cnt += 1
            res += c
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, c]
        return res