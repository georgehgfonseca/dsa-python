from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        def square(n):
            return n * n
        
        def helper(x, n):
            if n == 0:
                return 1
            newN = n // 2
            if n % 2 == 0:
                return square(helper(x, newN))
            else:
                return square(helper(x, newN)) * x
        if n < 0:
            n = -n
            return 1 / helper(x, n)
        return helper(x, n)


testCases = [
    (0.00001, 2147483647),
    (0.44528, 0),
    (2, 3),
    # res : 8
    # i   : 2
    (2, 10),  
    (2.1, 3), 
    (2, -2),  
]

s = Solution()
for t in testCases:
    print(s.myPow(t[0], t[1]))
