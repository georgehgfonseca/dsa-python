from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = digits[:]
        buffer = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 + buffer > 9:
                ans[i] = 0
                buffer = 1
            else:
                ans[i] += 1
                return ans
        if buffer == 1:
            ans = [1] + ans
        return ans


testCases = [[1, 2, 3], [4, 3, 2, 1], [9]]
s = Solution()
for t in testCases:
    print(s.plusOne(t))
