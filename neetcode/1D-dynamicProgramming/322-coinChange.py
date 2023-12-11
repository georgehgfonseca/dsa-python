from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        valueMinCoins = {i:float("inf") for i in range(1, amount + 1)}
        for coin in coins:
            valueMinCoins[coin] = 1
        valueMinCoins[0] = 0

        for value in range(1, amount + 1):
            for c in coins:
                if value - c > 0:
                    valueMinCoins[value] = min(valueMinCoins[value], 1 + valueMinCoins[value - c])

        if valueMinCoins[amount] == float("inf"):
            return -1
        return valueMinCoins[amount]

        # coins.sort(reverse=True)

        # # minDepth = {coin:1 for coin in coins}
        # minDepth = {}
        # def helper(cur, numCoins):
        #     if cur in minDepth:
        #         minDepth[cur] = min(minDepth[cur], numCoins)
        #         return
        #     minDepth[cur] = numCoins
        #     if cur == amount:
        #         # achieved the amount
        #         return
        #     if cur < amount:
        #         for coin in coins:
        #             if cur + coin <= amount:
        #                 # if (cur + coin) not in minDepth or minDepth[cur + coin] > numCoins + 1:
        #                 helper(cur+coin, numCoins+1)

        # helper(0, 0)
        # if amount not in minDepth:
        #     return -1
        # return minDepth[amount]

testCases = [
    ([1,2,5], 11), # 3
    ([186,419,83,408], 6249) # 20
]

s = Solution()
for t in testCases:
    print(s.coinChange(t[0], t[1]))