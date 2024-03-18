from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        index_maxprofit = dict({0: nums[0], 1: max(nums[0], nums[1])})

        for i in range(2, len(nums)):
            index_maxprofit[i] = max(index_maxprofit[i - 2] + nums[i], index_maxprofit[i - 1])

        return index_maxprofit[len(nums) - 1]

testCases = [
         [1,2,3,1],  # 4
]



s = Solution()
for t in testCases:
    print(s.rob(t))