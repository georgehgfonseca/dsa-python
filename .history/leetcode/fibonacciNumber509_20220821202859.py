from typing import List


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


testCases = [5]
s = Solution()
for t in testCases:
    print(s.fib(t))
