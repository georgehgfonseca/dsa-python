from typing import List
import heapq

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TODO: needed to watch the video
        if len(nums) == 2:
            return [nums[1], nums[0]]
            
        prefix = []
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(num)
            else:
                prefix.append(prefix[-1] * num)
        sulfix = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                sulfix.append(nums[i])
            else:
                sulfix.insert(0, sulfix[0] * nums[i])
        print(prefix, sulfix)

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(1 * sulfix[i + 1])
            elif i == len(nums) - 1:
                ans.append(1 * prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * sulfix[i + 1])
        
        return ans


    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        # uses division which is not allowed in the follow up
        overallProduct = 1
        zeroIdxs = set()
        for i, num in enumerate(nums):
            if num == 0:
                zeroIdxs.add(i)
                continue
            overallProduct *= num

        if len(zeroIdxs) > 1:
            # For edge cases such as [0, 8, 0] and [0, 0]
            return [0] * len(nums)

        ans = []
        for i, num in enumerate(nums):
            if num == 0:
                ans.append(overallProduct)
            elif zeroIdxs:
                ans.append(0)
            else:
                ans.append(int(overallProduct / num))
        return ans


test_cases = [
    [1,2,3,4],       # [24,12,8,6]
    # [-1,1,0,-3,3],   # [0,0,9,0,0]
]

s = Solution()
for t in test_cases:
    print(s.productExceptSelf(t))

