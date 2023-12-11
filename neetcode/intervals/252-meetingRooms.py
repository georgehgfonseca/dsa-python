from typing import List

class Solution:

    def meetingRooms(self, intervals: List[List[int]]) -> bool:
        # check if there is an overlap in the intervals
        intervals.sort(key=lambda x:x[0])
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < prevEnd:
                # they overlap
                return False
            prevEnd = max(prevEnd, end)

        return True


testCases = [
    [[0,30],[5,10],[15,20]],    # False
    [[7,10],[2,4]], # True
]

s = Solution()
for t in testCases:
    print(s.meetingRooms(t))