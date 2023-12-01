from typing import List

class Solution:

    def trap(self, height: List[int]) -> int:
        # needed a help from the video to get the idea
        if len(height) < 3:
            return 0
        
        # map containing, for each elem, the max height on its sides
        max_left_height = {0: 0}
        max_right_height = {len(height) - 1: 0}

        curr_max_left = 0
        for i in range(1, len(height)):
            curr_max_left = max(curr_max_left, height[i-1])
            max_left_height[i] = curr_max_left

        curr_max_right = 0
        for i in range(len(height) - 2, -1, -1):
            curr_max_right = max(curr_max_right, height[i+1])
            max_right_height[i] = curr_max_right

        trapped_water = 0
        for i in range(len(height)):
            water = min(max_left_height[i], max_right_height[i]) - height[i]
            water = max(0, water)
            trapped_water += water

        return trapped_water


testCases = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [1,2,8,6,2,5,4,8,3,7], # 49 
    [1,6],               # 5 
    [1,6,1,1,6],         # 18
    [0, 0, 0]]           # 0

s = Solution()
for t in testCases:
    print(s.trap(t))