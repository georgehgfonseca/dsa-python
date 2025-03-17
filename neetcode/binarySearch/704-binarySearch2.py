from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
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