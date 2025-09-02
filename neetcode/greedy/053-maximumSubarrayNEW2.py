class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy - if curr sum is negative, move pointer to next subarray start
        res = nums[0]
        curr = 0
        i = 0
        while i < len(nums):
            curr += nums[i]
            res = max(res, curr)
            if curr < 0:
                curr = 0
            i += 1
        return res