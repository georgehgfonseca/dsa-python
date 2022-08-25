from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = digits[:]
        buffer = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 + buffer > 9:
                digits[i] = 0
                buffer = 1
        if buffer == 1:
            ans = [1] + ans
        return ans


testCases = [[1, 2, 3]]
s = Solution()
for t in testCases:
    print(s.plusOne(t))
