from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:
        # had to see neetcode video
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                # subproblem is sorted
                res = min(res, nums[left])
                break
            
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res

testCases = [
    [3,4,5,1,2],
    [4,5,6,7,0,1,2],
]

s = Solution()
for t in testCases:
    print(s.findMin(t))