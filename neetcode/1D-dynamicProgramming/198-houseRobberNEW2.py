class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {0: nums[0], 1: max(nums[0], nums[1])}

        for i in range(2, len(nums)):
            cache[i] = max(cache[i - 2] + nums[i], cache[i - 1])
        
        return cache[len(nums) - 1]