from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float("inf")
        minI = -1
        max = -1
        maxI = -1
        while min != max:
            min = float("inf")
            minI = -1
            max = -1
            maxI = -1
            for i in range(len(prices)):
                if prices[i] < min:
                    min = prices[i]
                    minI = i
            for i in range(len(prices)):
                if prices[i] > min:
                    max = prices[i]
                    maxI = i
            if minI < maxI:
                return max - min
        return 0

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
