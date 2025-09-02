from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                return False
            i += nums[i]
            if i >= len(nums) - 1:
                return True
        return False


testCases = [
    [1,2,0,1,0], # true
    [1,2,1,0,1], # false
    [2,3,1,1,4],
    [3,2,1,0,4],
]

s = Solution()
for t in testCases:
    print(s.canJump(t))