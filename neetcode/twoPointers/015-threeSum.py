from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        complement_index = {nums[i]: i for i in range(len(nums))}
        triplets = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in complement_index:
                    k = complement_index[complement]
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    triplet = tuple(triplet)
                    all_indexes_different = i != j and i != k and j != k
                    if all_indexes_different and triplet not in triplets:
                        triplets.add(triplet)

        return [list(triplet) for triplet in triplets]

testCases = [
    [-1,0,1,2,-1,-4], 
    [0, 0, 0]]

s = Solution()
for t in testCases:
    print(s.threeSum(t))