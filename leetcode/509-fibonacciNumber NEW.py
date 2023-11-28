class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memo = [1, 1]
        for i in range(2, n):
            new = memo[0] + memo[1]
            memo[0], memo[1] = memo[1], new
        return memo[1]
        


testCases = [10]
s = Solution()
for t in testCases:
    print(s.fib(t))
