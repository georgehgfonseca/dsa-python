from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        dp[0] = [0, prices[0]]  # current profit, current price
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], prices[i] - dp[i - 1][1])
            dp[i][1] = min(dp[i - 1][1], prices[i])
        return dp[-1][0]

    def maxProfitSlow(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max


testCases = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
s = Solution()
for t in testCases:
    print(s.maxProfit(t))
