class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1
        for i in range(2, x):
            if i * i <= x:
                ans = i
            else:
                break
        return ans


testCases = [4, 8]
s = Solution()
for t in testCases:
    print(s.mySqrt(t))
