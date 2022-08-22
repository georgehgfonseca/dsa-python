from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [1 for _ in range(target + 1)]
        for i in range(2, target + 1):
            dp[i] = dp[i - 1] + i - 1

        return dp[target]


testCases = [([1, 2, 3], 4)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
