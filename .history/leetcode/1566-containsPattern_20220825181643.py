from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:

        max = 0
        for k in range(1, len(sequence) // len(word) + 1):
            wordK = word * k
            if wordK in sequence:
                max = k
            else:
                return max
        return False


testCases = [([1, 2, 4, 4, 4, 4], 1, 3)]
s = Solution()
for t in testCases:
    print(s.containsPattern(t[0], t[1], t[2]))
