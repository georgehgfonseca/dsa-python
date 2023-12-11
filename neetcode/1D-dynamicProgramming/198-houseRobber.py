from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        robPrev = 0
        robPrevPrev = 0
        for n in nums:
            temp = max(robPrev, robPrevPrev + n)
            robPrevPrev = robPrev
            robPrev = temp
        
        return robPrev

testCases = [
         [1,2,3,1],  # 4
]



s = Solution()
for t in testCases:
    print(s.rob(t))