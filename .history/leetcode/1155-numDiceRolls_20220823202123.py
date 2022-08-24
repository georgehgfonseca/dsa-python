from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(1, target + 1):
            for face in range(1, k + 1):
                if i + face < len(dp):
                    dp[i + face] += dp[i] + 1
        return dp[target + 1]


testCases = [(1, 6, 3)]
s = Solution()
for t in testCases:
    print(s.numRollsToTarget(t[0], t[1], t[2]))
