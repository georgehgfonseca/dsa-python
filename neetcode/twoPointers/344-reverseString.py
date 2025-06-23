from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            aux = s[i]
            s[i] = s[-i - 1]
            s[-i - 1] = aux


testCases = ["hello world!"]

s = Solution()
for t in testCases:
    print(s.reverseString(t))
