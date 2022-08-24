from typing import List


class Solution:
    mod = 1000000007

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1  # way to get sum 0
        for rep in range(1, n + 1):
            newdp = [0 for i in range(target + 1)]
            for already in range(0, target + 1):
                for pipes in range(1, k + 1):
                    if already + pipes <= target:
                        newdp[already + pipes] = (newdp[already + pipes] + dp[already]) % mod
            dp = newdp
        return int(dp[target] % mod)


testCases = [(2, 6, 7)]
s = Solution()
for t in testCases:
    print(s.numRollsToTarget(t[0], t[1], t[2]))
