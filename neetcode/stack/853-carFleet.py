from typing import List
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_arrival = [[position[i], speed[i], (target - position[i]) / speed[i], True] for i in range(len(position))]
        pos_speed_arrival.sort(reverse=True)
        for i in range(len(pos_speed_arrival)):
            if not pos_speed_arrival[i][3]:
                continue
            for j in range(i + 1, len(pos_speed_arrival)):
                will_collide = pos_speed_arrival[i][2] >= pos_speed_arrival[j][2]
                if will_collide:
                    pos_speed_arrival[j][3] = False
                else:
                    break
        ans = 0
        for elem in pos_speed_arrival:
            if elem[3]:
                ans += 1
        return ans

                     
testCases = [
    (12, [10,8,0,5,3], [2,4,1,1,3]),
    (10, [4,1,0,7], [2,2,1,1]),
    (10, [1,4], [3,2]),
] 

s = Solution()
for t in testCases:
    print(s.carFleet(t[0], t[1], t[2]))
