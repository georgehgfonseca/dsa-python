class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        pending = []
        n = len(nums)
        res = [-1] * n
        for i in range(2 * n):
            while pending and nums[i % n] > pending[-1][0]:
                num, j = pending.pop()
                res[j] = nums[i % n]
            pending.append((nums[i % n], i % n))
        return res