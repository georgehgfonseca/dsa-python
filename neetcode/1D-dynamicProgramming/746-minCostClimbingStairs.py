from typing import List

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        memo = [cost[0], cost[1]]

        for i in range(2, len(cost)+1):
            if i >= len(cost):
                cost_i = min(memo[0], memo[1])
            else:
                cost_i = min(memo[0], memo[1]) + cost[i]
            memo[0], memo[1] = memo[1], cost_i

        return min(memo[0], memo[1])

# n cost to get to the index plus cost of index

# n(0) = 10                          -> 10
# n(1) = 15                          -> 15
# n(2) = min(n(0), n(1)) + cost[2]   -> 10+20 = 30
# n(3) = min(n(1), n(2)) + cost[3]   -> 15+none = 15

testCases = [
    [10,15,20],                   # 15
    [1,100,1,1,1,100,1,1,100,1],  # 6
]

s = Solution()
for t in testCases:
    print(s.minCostClimbingStairs(t))