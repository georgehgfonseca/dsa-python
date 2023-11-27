from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count_not_equal = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
                count_not_equal += 1
        return count_not_equal

testCases = [([3,2,2,3], 3), ([0,1,2,2,3,0,4,2], 2), ([3, 3], 3)]
s = Solution()
for t in testCases:
    print(s.removeElement(t[0], t[1]))
