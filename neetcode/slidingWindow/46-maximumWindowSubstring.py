from typing import List

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        pass


testCases = [
    ("ab", "eidbaooo"),    # True
    ("ab", "eidboaoo"),    # False
]

s = Solution()
for t in testCases:
    print(s.checkInclusion(t[0], t[1]))