from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1)] * (len(coins) + 1)

        for i in range(len(coins) + 1):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(coins)][amount]

        # for i in range(1, amount + 1):
        #     c = 0
        #     while c < len(coins):
        #         dp[i + coins[c]][c]
        #         if dp[i - coins[c]][c] + coins[c] == dp[i][c]:
        #             dp[i][c]
        #         if i - coins[c] >= 0:
        #             dp[i][c] += dp[i - 1][c] + 1
        # if dp[amount] == float("inf"):
        #     return -1
        # return dp[amount]


testCases = [(5, [1, 2, 5])]
s = Solution()
for t in testCases:
    print(s.change(t[0], t[1]))
