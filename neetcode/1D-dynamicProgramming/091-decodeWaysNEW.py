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
