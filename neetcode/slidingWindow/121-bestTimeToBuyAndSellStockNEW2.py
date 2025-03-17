from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        min_value = prices[l]
        max_value = prices[r]
        while r < len(prices):
            if prices[r] < min_value:
                min_value = prices[r]
                l = r
            if prices[l] < min_value:
                min_value = prices[l]
            if prices[r] > max_value:
                max_value = prices[r]
            r += 1

        return max(0, max_value - min_value)


testCases = [
    [7,1,5,3,6,4],         # 5 
    [1,2,8,6,2,5,4,8,3,7], # 7 
    [1,6],                 # 5 
    [1,6,1,1,6],           # 5
    [0, 0, 0]]             # 0

s = Solution()
for t in testCases:
    print(s.maxProfit(t))