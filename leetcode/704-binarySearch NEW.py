from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = ((high - low) // 2) + low
            print(low, mid, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1 

testCases = [([5], 5), ([-1, 0, 3, 5, 9, 12], 9), ([-1, 0, 3, 5, 9, 12], 2), ([-1,0,3,5,9,12], 13)]
s = Solution()
for t in testCases:
    print(s.search(t[0], t[1]))
