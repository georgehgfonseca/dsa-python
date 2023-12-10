from typing import List

class Solution:
    def reverseBits(self, n: int) -> int:
        # copied from neetcode
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

testCases = [
    int("00000010100101000001111010011100", 2)
]

s = Solution()
for t in testCases:
    print(s.reverseBits(t))