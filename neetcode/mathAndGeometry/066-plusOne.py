from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        offset = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + offset == 10:
                digits[i] = 0
                offset = 1
            else:
                digits[i] += offset
                offset = 0
        if offset:
            digits.insert(0, 1)
        return digits
        
testCases = [
    [1,2,3],  # [1,2,4]
    [9,9,9],  # [1,0,0,0]
]

s = Solution()
for t in testCases:
    print(s.plusOne(t))
