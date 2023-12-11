from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        # copied from neetcode
        LIS = [1 for num in nums]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)


testCases = [
[10,9,2,5,3,7,101,18] # 4
]

s = Solution()
for t in testCases:
    print(s.lengthOfLIS(t))