from typing import List

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        prevEnd = intervals[0][1]

        res = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            # check if they overlap
            if start < prevEnd:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = max(prevEnd, end)
        return res


testCases = [
    [[1,2],[2,3],[3,4],[1,3]],    # 1
    [[0,2],[1,3],[2,4],[3,5],[4,6]],    # 2
]

s = Solution()
for t in testCases:
    print(s.eraseOverlapIntervals(t))