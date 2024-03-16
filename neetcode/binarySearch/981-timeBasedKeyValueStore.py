from typing import List
import math

class TimeMap:

    def __init__(self):
        self.key_timestamps_map = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_timestamps_map:
            self.key_timestamps_map[key] = []
        self.key_timestamps_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.key_timestamps_map.get(key, [])

        # binary search
        r = len(values) - 1
        l = 0
        while r >= l:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))  # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))         # return "bar"
print(timeMap.get("foo", 3))         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
print(timeMap.set("foo", "bar2", 4)) # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))         # return "bar2"
print(timeMap.get("foo", 5))         # return "bar2"