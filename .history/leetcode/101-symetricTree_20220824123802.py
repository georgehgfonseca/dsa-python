class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        for i in range(1, x + 1):
            if i * i <= x:
                ans = i
            else:
                break
        return ans


testCases = [4, 8, 1, 16, 10, 0]
s = Solution()
for t in testCases:
    print(s.mySqrt(t))
