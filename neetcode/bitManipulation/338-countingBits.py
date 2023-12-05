from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for elem in range(n):
            res.append(int(elem, 2))
        return res


testCases = [
    2,  # [0, 1, 1]
    5,  # [0, 1, 1, 2, 1, 2]
]

s = Solution()
for t in testCases:
    print(s.countBits(t))