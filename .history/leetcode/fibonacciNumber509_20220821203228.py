from typing import List


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = [0, 1]
        for i in range(1, n):
            temp = a[0]
            a[0] = a[1]
            a[1] = a[0] + temp
        return a[1]

    def fibSlow(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


testCases = [10]
s = Solution()
for t in testCases:
    print(s.fib(t))
