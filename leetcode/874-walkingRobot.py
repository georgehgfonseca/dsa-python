from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curr_x, curr_y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0
        res = 0
        obstacles_set = {tuple(obstacle) for obstacle in obstacles}

        for c in commands:
            if c == -1:
                direction_index = (direction_index + 1) % len(directions)
            elif c == -2:
                direction_index = (direction_index - 1) % len(directions)
            else:
                for _ in range(c):
                    if (curr_x + directions[direction_index][0], curr_y + directions[direction_index][1]) in obstacles_set:
                        break
                    curr_x, curr_y = curr_x + directions[direction_index][0], curr_y + directions[direction_index][1]
            
            res = max(res, curr_x**2 + curr_y**2)

        return res

testCases = [([4,-1,3], []), ([4,-1,4,-2,4], [[2,4]]), ([6,-1,-1,6], [])]
s = Solution()
for t in testCases:
    print(s.robotSim(t[0], t[1]))
