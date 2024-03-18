from typing import List

class Solution:

    def climbStairs(self, n: int) -> int:
        stairs_ways = {1: 1, 2: 2}
        for i in range(3, n + 1):
            stairs_ways[i] = stairs_ways[i - 1] + stairs_ways[i - 2]
        return stairs_ways[n]




testCases = [
    2,  # 2
    3,  # 3
    5,  # 8
]

s = Solution()
for t in testCases:
    print(s.climbStairs(t))