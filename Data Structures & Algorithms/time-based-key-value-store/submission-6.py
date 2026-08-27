class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        key = self.keys[key]
        if not key:
            return ""
        
        l, r = 0, len(key) - 1
        resStmp = float('-inf')
        res = ""

        while l <= r:
            mp = (l + r) // 2
            if key[mp][1] == timestamp:
                return key[mp][0]
            if key[mp][1] < timestamp:
                resStmp = max(resStmp, key[mp][1])
                if resStmp == key[mp][1]: res = key[mp][0]
                l = mp + 1
            else:
                r = mp - 1
        
        return res

