from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TODO: copied solution (https://www.youtube.com/watch?v=Hdr64lKQ3e4&ab_channel=TechWithNikola)

        memo = [float("inf")] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], memo[i - coin] + 1)

        if memo[amount] == float("inf"):
            return -1
        else:
            return memo[amount]


testCases = [([2], 3), ([1], 0), ([1, 2, 5], 11)]
s = Solution()
for t in testCases:
    print(s.coinChange(t[0], t[1]))
