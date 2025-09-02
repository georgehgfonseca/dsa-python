class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestLeft = {0: float("inf"), 1: prices[0]}
        for i in range(2, len(prices)):
            lowestLeft[i] = min(prices[i - 1], lowestLeft[i - 1])

        maxDiff = 0
        for i in range(len(prices)):
            diff = prices[i] - lowestLeft[i]
            maxDiff = max(maxDiff, diff)

        return maxDiff
        