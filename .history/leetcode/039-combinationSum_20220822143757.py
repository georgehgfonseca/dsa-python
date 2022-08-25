from typing import List


class Solution:
    def combinationSum4(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for x in candidates:
                if i - x >= 0:
                    dp[i] += dp[i - x]
        return dp[target]


testCases = [([1, 2, 5], 5)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
