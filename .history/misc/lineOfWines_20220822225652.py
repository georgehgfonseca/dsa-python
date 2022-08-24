# Based on https://www.youtube.com/watch?v=pwpOC1dph6U&ab_channel=Errichto

from typing import List


class Solution:
    def lineOfWines(self, arr: List[int]) -> int:
        # todo handle edge cases (len = 1)
        # base case
        dp = [[0 for _ in range(len(arr) + 1)] for _ in range(len(arr) + 1)]
        # dp[0][len(arr) - 2] = arr[len(arr) - 1]
        # dp[1][len(arr) - 1] = arr[0]
        for l in range(len(arr) + 1):
            for r in range(len(arr), -1, -1):
                if l == 0 and r == len(arr):
                    continue
                year = l + len(arr) - r
                dp[l][r] = max(year * arr[l] + dp[l - 1][r], year * arr[r] + dp[l][r + 1])

        return dp[0][0]


testCases = [[2, 4, 6, 2, 5]]
s = Solution()
for t in testCases:
    print(s.lineOfWines(t))
