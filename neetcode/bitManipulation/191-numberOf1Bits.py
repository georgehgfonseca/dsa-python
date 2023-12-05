from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res


testCases = [
    int("00000000000000000000000000001011", 2),  # 3
    int("00000000000000000000000010000000", 2),  # 1
    int("11111111111111111111111111111101", 2),  # 31
]

s = Solution()
for t in testCases:
    print(s.hammingWeight(t))