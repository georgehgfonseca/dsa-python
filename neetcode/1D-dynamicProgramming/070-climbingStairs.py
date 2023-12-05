from typing import List

class Solution:

    def climbStairs(self, n: int) -> int:
        # base cases n(0) and n(1) 
        memo = [1, 1]
        if n == 0:
            return memo[0]
        if n == 1:
            return memo[1]
        
        for i in range(2, n+1):
            steps_i = memo[0] + memo[1]
            memo[0], memo[1] = memo[1], steps_i
        
        return memo[1]


testCases = [
    2,  # 2
    3,  # 3
    5,  # 8
]

s = Solution()
for t in testCases:
    print(s.climbStairs(t))