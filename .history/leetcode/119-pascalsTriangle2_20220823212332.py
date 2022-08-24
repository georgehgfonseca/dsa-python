from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        dp = [[] for i in range(rowIndex)]
        dp[0] = [1]
        dp[1] = [1, 1]
        for i in range(2, rowIndex):
            new = [1]
            for j in range(1, len(dp[i - 1])):
                new.append(dp[i - 1][j - 1] + dp[i - 1][j])
            new.append(1)
            dp[i] = new
        return dp[-1]


testCases = [3, 0, 1]
s = Solution()
for t in testCases:
    print(s.generate(t))
