from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [1]
        dp = [[] for i in range(numRows)]
        dp[0] = [1]
        dp[1] = [1, 1]
        for i in range(2, numRows):
            new = [1]
            for j in range(1, len(dp[i - 1])):
                new.append(dp[i - 1][j - 1] + dp[i - 1][j])
            new.append(1)
            dp[i] = new
        return dp


testCases = [5, 1]
s = Solution()
for t in testCases:
    print(s.generate(t))
