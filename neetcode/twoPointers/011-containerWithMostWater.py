from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_water = 0
        while start < end:
            water = (end - start) * min(height[start], height[end])
            max_water = max(max_water, water)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_water
    
        # O(n^2) solution - just for practice
        # max_water = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         water = (j - i) * min(height[i], height[j])
        #         max_water = max(max_water, water)

        # return max_water


testCases = [
    [1,8,6,2,5,4,8,3,7],   # 49 
    # start:     0
    # end:       8
    # water:     8 * 1
    # max_water: 8
    [1,2,8,6,2,5,4,8,3,7], # 49 
    [1,6],               # 5 
    [1,6,1,1,6],         # 18
    [0, 0, 0]]           # 0

s = Solution()
for t in testCases:
    print(s.maxArea(t))