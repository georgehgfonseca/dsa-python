from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of_complement = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in index_of_complement:
                return (i, index_of_complement[nums[i]])
            
            index_of_complement[complement] = i


test_cases = [([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6)]
s = Solution()
for t in test_cases:
    print(s.twoSum(t[0], t[1]))

