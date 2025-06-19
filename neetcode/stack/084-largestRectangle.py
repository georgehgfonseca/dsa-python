from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # TODO: needed to watch the video and some of the implementation
        stack = deque() # (index, height)
        maxArea = 0
        for i in range(1, len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                (topIdx, topHeight) = stack.pop()
                maxArea = max(maxArea, topHeight * (i - topIdx))
                start = topIdx
            stack.append((start, heights[i]))
        
        while stack:
            # compute heights that extend from its index all the way through the end
            (topIdx, topHeight) = stack.pop()
            area = topHeight * (len(heights) - topIdx)
            maxArea = max(maxArea, area)
            
        return maxArea
                     
    def largestRectangleAreaTO(self, heights: List[int]) -> int:
        # brute force
        maxArea = heights[0]
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                minHeight = min(heights[i:j + 1])
                currArea = minHeight * (j - i + 1)
                maxArea = max(maxArea, currArea)
        return maxArea
                     
testCases = [
    [2, 1, 5, 6, 2, 3],
    [7, 1, 7, 2, 2, 4],
] 

s = Solution()
for t in testCases:
    print(s.largestRectangleArea(t))
