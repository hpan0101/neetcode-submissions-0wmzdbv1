class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyStore.get(key)
        if not values:
            return ""
        res = ""
        l, r = 0, len(values) - 1
        while l <= r :
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res