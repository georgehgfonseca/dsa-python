from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution must use constant extra space (i.e. no dict allowed)
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i, j]
            if numbers[i] + numbers[j] < target:  # increase sum
                i += 1
            else:  # decrease sum
                j -= 1
        return [0, 0]  # should not reach here


testCases = [([2, 7, 11, 15], 9), ([2, 3, 4], 6), ([-1, 0], -1)]
s = Solution()
for t in testCases:
    print(s.twoSum(t[0], t[1]))
