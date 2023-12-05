from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        present_nums = set()
        for num in nums:
            present_nums.add(num)

        for i in range(len(nums) + 1):
            if i not in present_nums:
                return i


testCases = [
    [3,0,1],             # 2
    [9,6,4,2,3,5,7,0,1], # 8
    [0,1]                # 2
]

s = Solution()
for t in testCases:
    print(s.missingNumber(t))