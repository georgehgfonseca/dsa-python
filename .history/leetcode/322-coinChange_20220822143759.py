from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(len(amount) + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c])
        return dp[amount]


testCases = [([1, 2, 5], 11)]
s = Solution()
for t in testCases:
    print(s.coinChange(t[0], t[1]))
