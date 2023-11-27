from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map that associates a value to its complement's index
        value_complement_index = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in value_complement_index:
                value_complement_index[complement] = i
            if nums[i] in value_complement_index and i != value_complement_index[nums[i]]:
                return [i, value_complement_index[nums[i]]]


testCases = [([3, 3], 6), ([2, 7, 11, 15], 9), ([3, 2, 4], 6)]
s = Solution()
for t in testCases:
    print(s.twoSum(t[0], t[1]))
