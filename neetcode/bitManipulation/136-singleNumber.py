from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found_nums = set()
        for num in nums:
            if num not in found_nums:
                found_nums.add(num)
            else:
                found_nums.remove(num)
        return next(iter(found_nums))


testCases = [
    [2,2,1],             # 1
    [6,5,7,6,7],         # 5
    [1],                 # 1
    [0,1,1]              # 0
]

s = Solution()
for t in testCases:
    print(s.singleNumber(t))