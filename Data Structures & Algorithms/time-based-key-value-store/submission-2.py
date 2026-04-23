class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:    
        item = self.store.get(key)
        values = [(timestamp, value)]
        if item:
            self.store[key]+= values
        else:
            self.store[key] = values

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        res = ""
        l, r = 0, len(values)-1
        cursor = 0
        while l<=r:
            cursor = mid = (l+r)//2
            if timestamp >= values[mid][0]:
                res = values[mid][-1]
                l = mid+1
            else:
                r = mid-1
        return res

        
