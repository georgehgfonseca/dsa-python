from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # TODO: copied solution
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, target, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]

        # Pruning some cases are not optmial yet
        # self.ans = 0
        # def helper(nums, curr_idx, curr_sum, remaining_val):
        #     if curr_idx == len(nums):
        #         if curr_sum == target:
        #             self.ans += 1
        #     elif curr_sum - target > remaining_val or curr_sum - target < -remaining_val:
        #         # It is impossible to achieve target with the remaining items
        #         return
        #     else:
        #         helper(nums, curr_idx + 1, curr_sum + nums[curr_idx], remaining_val - nums[curr_idx])
        #         helper(nums, curr_idx + 1, curr_sum - nums[curr_idx], remaining_val - nums[curr_idx])

        # if not nums:
        #     return 0

        # remaining_val = sum(nums)        
        # helper(nums, 0, 0, remaining_val)
        # return self.ans

        # Time Limit Exceeded
        # self.ans = 0
        # def helper(nums, curr_idx, curr_sum):
        #     if curr_idx == len(nums):
        #         if curr_sum == target:
        #             self.ans += 1
        #     else:
        #         helper(nums, curr_idx + 1, curr_sum + nums[curr_idx])
        #         helper(nums, curr_idx + 1, curr_sum - nums[curr_idx])

        # if not nums:
        #     return 0
        
        # helper(nums, 0, 0)
        # return self.ans


testCases = [([1,1,1,1,1], 3), ([1], 1), ([3, 3], 6), 
             ([40,21,33,25,8,20,35,9,5,27,0,18,50,21,10,28,6,19,47,15], 3), 
             ([2,7,9,13,27,31,37,3,2,3,5,7,11,13,17,19,23,29,47,53], 17), 
             ([2,7,9,13,27,31,37,3,2,3,5,7,11,13,17,19,23,29,47,53], 7), 
             ([46,49,5,7,5,21,27,4,4,27,45,24,7,22,25,5,38,14,50,28], 45)]
s = Solution()
for t in testCases:
    print(s.findTargetSumWays(t[0], t[1]))
