class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0, 1, 2]:
            return n

        memo = [1, 2]
        for i in range(3, n + 1):
            new = memo[1] + memo[0]
            memo[0], memo[1] = memo[1], new
        return memo[1]



testCases = [3]
s = Solution()
for t in testCases:
    print(s.climbStairs(t))
