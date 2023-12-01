from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if len(prices) < 3:
            return max(0, prices[1] - prices[0])

        max_right_per_index = {len(prices) - 2: prices[-1]}
        max_right = prices[-1]
        for i in range(len(prices) - 3, -1, -1):
            max_right = max(prices[i + 1], max_right)
            max_right_per_index[i] = max_right
        
        max_diff = 0
        for i in range(len(prices) - 1):
            diff = max_right_per_index[i] - prices[i]
            max_diff = max(max_diff, diff)

        return max_diff

testCases = [
    [7,1,5,3,6,4],   # 5 
    #6 6 6 6 4
    # i:         1
    # max_right: 6
    # max_diff:  5
    [1,2,8,6,2,5,4,8,3,7], # 49 
    [1,6],               # 5 
    [1,6,1,1,6],         # 18
    [0, 0, 0]]           # 0

s = Solution()
for t in testCases:
    print(s.maxProfit(t))