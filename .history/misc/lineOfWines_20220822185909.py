# Based on https://www.youtube.com/watch?v=pwpOC1dph6U&ab_channel=Errichto

from typing import List


class Solution:
    def lineOfWines(self, arr: List[int]) -> int:
        # todo handle edge cases (len = 1)
        # base case
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        dp[0][len(arr) - 2] = arr[len(arr) - 1]
        dp[1][len(arr) - 1] = arr[0]
        for l in range(len(arr)):
            for r in range(len(arr) - 1, -1, -1):
                if l + 1 <= len(arr) - 1 and r - 1 >= 0:
                    year = l + len(arr) - 1 - r + 1
                    dp[l][r] = max(year * arr[l] + dp[l + 1][r], year * arr[r] + dp[l][r - 1])
                elif l + 1 <= len(arr) - 1 and r - 1 < 0:
                    year = l + len(arr) + 1
                    dp[l][r] = year * arr[l] + dp[l + 1][r]
                elif l + 1 > len(arr) - 1 and r - 1 >= 0:
                    year = len(arr) - 1 - r + 1
                    dp[l][r] = year * arr[r] + dp[l][r - 1]

        # for i in range(len(coins) + 1):
        #     for j in range(amount + 1):
        #         if j == 0:
        #             dp[i][j] = 1

        # for i in range(1, len(coins) + 1):
        #     for j in range(1, amount + 1):
        #         if j >= coins[i - 1]:
        #             dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j]

        return dp[0][0]


testCases = [[2, 4, 6, 2, 5]]
s = Solution()
for t in testCases:
    print(s.lineOfWines(t))
