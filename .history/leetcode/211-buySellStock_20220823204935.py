from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
