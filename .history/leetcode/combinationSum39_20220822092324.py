class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        last = [1, 2]
        for i in range(2, n):
            new = last[0] + last[1]
            last[0] = last[1]
            last[1] = new
        return last[1]


testCases = [3]
s = Solution()
for t in testCases:
    print(s.climbStairs(t))
