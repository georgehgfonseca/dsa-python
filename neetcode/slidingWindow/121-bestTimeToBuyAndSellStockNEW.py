from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        lowest = prices[0]
        max_diff = 0
        for price in prices:
            if price < lowest:
                lowest = price
            max_diff = max(max_diff, price - lowest)

        return max_diff




        # brute force
        max_diff = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_diff = max(max_diff, prices[j] - prices[i])
        return max_diff


testCases = [
    [7,1,5,3,6,4],         # 5 
    [1,2,8,6,2,5,4,8,3,7], # 49 
    [1,6],                 # 5 
    [1,6,1,1,6],           # 18
    [0, 0, 0]]             # 0

s = Solution()
for t in testCases:
    print(s.maxProfit(t))