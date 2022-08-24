from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] number of coins for ballon i bursted at j-th time
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
        dp[0][len(nums) - 1] = nums[0]
        for i in range(len(nums)):
            for j in range(len(nums) - 1, -1, -1):
                maxCoins = dp[i][j]
                for k in range(len(nums)):
                    maxK = dp[i][j] + nums[i] * nums[k] * 1
        return 0


testCases = [[3, 1, 5, 8]]
s = Solution()
for t in testCases:
    print(s.maxCoins(t))
