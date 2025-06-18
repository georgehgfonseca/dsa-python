from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)
        return maxProfit

        # brute force
        maxProfit = 0
        for l in range(len(prices)):
            for r in range(l + 1, len(prices)):
                maxProfit = max(maxProfit, prices[r] - prices[l])
        return maxProfit
        # l and r pointers
        # r moves when = i or prices[r + 1] is higher than prices[r]
        # l moves when l + 1 is smaller or r didn't move
        l = r = 0
        maxProfit = 0
        while l < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if r + 1 >= len(prices):
                l += 1
                continue

            if r == l or prices[r + 1] > prices[r]:
                r += 1
                continue
            
            l += 1

        return maxProfit

testCases = [
    [7,1,5,3,6,4],         # 5 
    [1,2,8,6,2,5,4,8,3,7], # 7 
    [1,6],                 # 5 
    [1,6,1,1,6],           # 5
    [0, 0, 0]]             # 0

s = Solution()
for t in testCases:
    print(s.maxProfit(t))