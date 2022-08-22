class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        last = [0, 1]
        for i in range(1, n):
            new = last[0] + last[1]
            last[0] = last[1]
            last[1] = new
        return last[1]


testCases = [3]
s = Solution()
for t in testCases:
    print(s.climbStairs(t))
