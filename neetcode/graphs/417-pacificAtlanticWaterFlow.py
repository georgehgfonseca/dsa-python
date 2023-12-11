from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # preprocess border cells
        canOverflowTopLeft = set()
        canOverflowBottomRight = set()
        for j in range(len(heights[0])):
            canOverflowTopLeft.add((0, j))
            canOverflowBottomRight.add((len(heights) - 1, j))
        for i in range(len(heights)):
            canOverflowTopLeft.add((i, 0))
            canOverflowBottomRight.add((i, len(heights[0]) - 1))

        def dfsTopLeft(i, j):
            if i == 0 or j == 0 or (i, j) in canOverflowTopLeft:
                canOverflowTopLeft.add((i, j))
                return True
            if i-1 >= 0 and heights[i-1][j] <= heights[i][j] and j-1 >= 0 and heights[i][j-1] <= heights[i][j]:
                return dfsTopLeft(i - 1, j) or dfsTopLeft(i, j - 1)
            if i-1 >= 0 and heights[i-1][j] <= heights[i][j]:
                return dfsTopLeft(i - 1, j)
            if j-1 >= 0 and heights[i][j-1] <= heights[i][j]:
                return dfsTopLeft(i, j - 1)
            return False
        
        def dfsBotRight(i, j):
            if i == len(heights) - 1 or j == len(heights[i]) - 1 or (i, j) in canOverflowBottomRight:
                canOverflowBottomRight.add((i, j))
                return True
            if i+1 < len(heights) and heights[i+1][j] <= heights[i][j] and j+1 < len(heights) and heights[i][j+1] <= heights[i][j]:
                return dfsBotRight(i + 1, j) or dfsBotRight(i, j + 1)
            if i+1 < len(heights) and heights[i+1][j] <= heights[i][j]:
                return dfsBotRight(i + 1, j)
            if j+1 < len(heights) and heights[i][j+1] <= heights[i][j]:
                return dfsBotRight(i, j + 1)
            return False
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if dfsTopLeft(i, j) and dfsBotRight(i, j):
                    res.append([i, j])
        
        return res

        # # process intern cells from top to bottom
        # for i in range(1, len(heights) - 1):
        #     for j in range(1, len(heights[i]) - 1):
        #         top = (i-1, j, heights[i-1][j])
        #         down = (i+1, j, heights[i+1][j])
        #         left = (i, j-1, heights[i][j-1])
        #         right = (i, j+1, heights[i][j+1])
        #         if heights[i][j] >= top[2] or heights[i][j] >= left[2]:
        #             if top in canOverflowTopLeft or left in canOverflowTopLeft:
        #                 canOverflowTopLeft.add((i, j, heights[i][j]))
        #         if heights[i][j] >= down[2] or heights[i][j] >= right[2]:
        #             if down in canOverflowBottomRight or right in canOverflowBottomRight:
        #                 canOverflowBottomRight.add((i, j, heights[i][j]))
        # # process intern cells from bottom to top
        # for i in range(len(heights) - 2, 0, -1):
        #     for j in range(1, len(heights[i]) - 1):
        #         top = (i-1, j, heights[i-1][j])
        #         down = (i+1, j, heights[i+1][j])
        #         left = (i, j-1, heights[i][j-1])
        #         right = (i, j+1, heights[i][j+1])
        #         if heights[i][j] >= top[2] or heights[i][j] >= left[2]:
        #             if top in canOverflowTopLeft or left in canOverflowTopLeft:
        #                 canOverflowTopLeft.add((i, j, heights[i][j]))
        #         if heights[i][j] >= down[2] or heights[i][j] >= right[2]:
        #             if down in canOverflowBottomRight or right in canOverflowBottomRight:
        #                 canOverflowBottomRight.add((i, j, heights[i][j]))


        # res = []
        # for cell in canOverflowBottomRight:
        #     if cell in canOverflowTopLeft:
        #         res.append([cell[0], cell[1]])

        # return res

    

testCases = [
    [[1,2,2,3,5],
     [3,2,3,4,4],
     [2,4,5,3,1],
     [6,7,1,4,5],
     [5,1,1,2,4]],
    [[1,2,3],
     [8,9,4],
     [7,6,5]]
]

s = Solution()
for t in testCases:
    print(s.pacificAtlantic(t))