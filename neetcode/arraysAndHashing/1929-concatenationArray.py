from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


test_cases = [
    [1, 2, 3],  # [1, 2, 3, 1, 2, 3]
]
s = Solution()
for t in test_cases:
    print(s.getConcatenation(t))
