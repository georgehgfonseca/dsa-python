from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # considers candidates = 1..len(candidates) + 1
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for x in candidates:
                dp[i] += dp[i - x]

        return dp[target]


testCases = [([1, 2, 3], 4)]
s = Solution()
for t in testCases:
    print(s.combinationSum(t[0], t[1]))
