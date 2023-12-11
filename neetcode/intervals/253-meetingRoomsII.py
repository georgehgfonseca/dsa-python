from typing import List

class Solution:

    def meetingRooms(self, intervals: List[List[int]]) -> bool:
        # brute force O(n^2)
        intervals.sort(key=lambda x:x[0])
        # for each interval group all intervals that does not overlap with it
        intervalOverlapping = {(start, end): set() for start, end in intervals}
        i = 0
        while i < len(intervals):
            startI, endI = intervals[i][0], intervals[i][1]
            for j in range(i+1, len(intervals)):
                startJ, endJ = intervals[j][0], intervals[j][1]
                if startJ < endI:
                    # they do overlap
                    intervalOverlapping[(startI, endI)].add((startJ, endJ))
                    intervalOverlapping[(startJ, endJ)].add((startI, endI))
                else:
                    i = j
            i += 1
        
        if len(intervals) == 0:
            return 0
        
        res = 1
        for interval in intervalOverlapping:
            res = max(res, len(intervalOverlapping[interval]))

        return res

testCases = [
    [[0,30],[5,10],[15,20]],    # 2
    [[7,10],[2,4]], # 1
]

s = Solution()
for t in testCases:
    print(s.meetingRooms(t))