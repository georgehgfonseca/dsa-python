from typing import List
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass

                     
testCases = [
    (12, [10,8,0,5,3], [2,4,1,1,3])
] 

s = Solution()
for t in testCases:
    print(s.carFleet(t[0], t[1], t[2]))
