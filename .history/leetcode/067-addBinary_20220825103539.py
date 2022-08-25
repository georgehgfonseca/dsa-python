from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        # fix dimensions
        length = max(len(a), len(b))
        if len(a) != length:
            a = "0" * (length - len(a)) + a
        if len(b) != length:
            b = "0" * (length - len(b)) + b
        for i in range(len(a) + 1, -1, -1):
            pass
        return 0


testCases = [("11", "1"), ("1010", "1011")]
s = Solution()
for t in testCases:
    print(s.twoSum(t[0], t[1]))
