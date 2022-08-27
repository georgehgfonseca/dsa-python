from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution must use constant extra space

        # runs in O(n)
        idxs = {}
        for i in range(len(nums)):
            if nums[i] not in idxs:
                idxs[nums[i]] = i
            if target - nums[i] in idxs and i != idxs[target - nums[i]]:
                return [i, idxs[target - nums[i]]]

    def twoSumSlow(self, nums: List[int], target: int) -> List[int]:
        # Runs in O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


testCases = [([2, 7, 11, 15], 9), ([2, 3, 4], 6), ([-1, 0], -1)]
s = Solution()
for t in testCases:
    print(s.twoSum(t[0], t[1]))
