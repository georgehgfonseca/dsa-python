# Based on https://www.youtube.com/watch?v=pwpOC1dph6U&ab_channel=Errichto

from typing import List


class Solution:
    def lineOfWines(self, arr: List[int]) -> int:
        # todo handle edge cases (len = 1)
        dp = [[0 for _ in range(len(arr) + 1)] for _ in range(len(arr) + 1)]

        # for l in range(len(arr), 0, -1):
        #     for r in range(l, len(arr)):
        #         dp[l][r] = max(dp[l+1][r])

        for l in range(len(arr) + 1):
            for r in range(len(arr), -1, -1):
                if l == 0 and r == len(arr):
                    continue  # ignore base case
                if l + len(arr) - r > len(arr):
                    continue  # invalid num of removals
                if r + 1 > len(arr):
                    year = l + len(arr) - r
                    dp[l][r] = year * arr[l - 1] + dp[l - 1][r]
                else:
                    year = l + len(arr) - r
                    dp[l][r] = max(year * arr[l] + dp[l - 1][r], year * arr[r] + dp[l][r + 1])

        return dp[0][0]


testCases = [[2, 4, 6, 2, 5]]
s = Solution()
for t in testCases:
    print(s.lineOfWines(t))
