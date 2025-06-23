from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        # can be decoded individually, or along with previous
        # dp[i] = 1 + dp[i - 1] if none are 0
        # dp[i] = 1 if s[i - 1] == 0
        # dp[i] = dp[i - 1] if s[i] == 0
        # edge cases "0" "00" "01" "10"
        if s[0] == "0" or "00" in s:
            return 0

        dp = [1]
        for i in range(1, len(s) - 1):
            if (
                (s[i - 1] == "1" or (s[i - 1] == "2" and int(s[i]) <= 6))
                and s[i] != "0"
                and s[i + 1] != "0"
            ):
                # can be decoded 2 ways
                dp.append(dp[-1] + dp[-2])
            else:
                dp.append(dp[-1])

        # process last position
        if s[-1] != "0" and 10 <= int(s[-2:]) <= 26:
            dp.append(dp[-1] + dp[-2])
        else:
            dp.append(dp[-1])
        return dp[-1]


testCases = ["1123", "12", "1201234"]

s = Solution()
for t in testCases:
    print(s.numDecodings(t))
