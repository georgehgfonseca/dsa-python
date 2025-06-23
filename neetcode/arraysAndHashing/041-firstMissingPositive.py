from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # using O(n) space
        nums = set(nums)

        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


test_cases = [
    [-1, 2, 4, 1], # 3
]

s = Solution()
for t in test_cases:
    print(s.firstMissingPositive(t))

