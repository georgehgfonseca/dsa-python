from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        # TODO had to aks gpt for a fix
        if not s or s[0] == '0':
            return 0

        n = len(s)
        waysUntilI = [0] * (n + 1)
        waysUntilI[0] = 1  # base case: empty string
        waysUntilI[1] = 1  # base case: first character (already checked it's not '0')

        for i in range(2, n + 1):
            if s[i-1] != '0':
                waysUntilI[i] += waysUntilI[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                waysUntilI[i] += waysUntilI[i - 2]

        return waysUntilI[n]


testCases = ["1123", "12", "1201234"]

s = Solution()
for t in testCases:
    print(s.numDecodings(t))
class Solution2:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = dict()
        dp[len(s)] = 1

        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                # can be decoded 2 ways
                dp[i] = dfs(i + 1) + dfs(i + 2)
                return dp[i]
            dp[i] = dfs(i + 1)
            return dp[i]
        
        dfs(0)
        return dp[0]
        
