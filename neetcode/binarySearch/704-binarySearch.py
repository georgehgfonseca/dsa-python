from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

testCases = [
    ([2,5], 5),             # 1
    ([5], 5),               # 0
    ([-1,0,3,5,9,12], 9),   # 4
    ([-1,0,3,5,9,12], 2)    # -1
]

s = Solution()
for t in testCases:
    print(s.search(t[0], t[1]))