from typing import List
import heapq

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {0: 1}
        sulfix = {len(nums) - 1: 1}

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            sulfix[i] = sulfix[i + 1] * nums[i + 1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * sulfix[i])
        return ans

test_cases = [
    [1,2,3,4],       # [24,12,8,6]
    [-1,1,0,-3,3]]   # [0,0,9,0,0]

s = Solution()
for t in test_cases:
    print(s.productExceptSelf(t))

