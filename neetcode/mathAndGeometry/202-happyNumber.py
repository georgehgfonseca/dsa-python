from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            newN = 0
            while n >= 10:
                newN += (n % 10) ** 2
                n = n // 10
            newN += (n % 10) ** 2
            n = newN
            if n == 1:
                return True
        return False
    
testCases = [
    19,  # True
    2,  # False
]

s = Solution()
for t in testCases:
    print(s.isHappy(t))
