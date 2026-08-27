class TimeMap:

    def __init__(self):
        self.d = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # binary search on timestamp
        vals = self.d.get(key, []) # if key dont exist return []
        l, r = 0, len(vals) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            # shrink to right, higher
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
            
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
make dictionary to store key: (value, timestamp)
run binary search on the timestamp
timestamp is increasing only
l, r = 0, len(d[key])
"""