from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[int]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
            

testCases = [
    [[0,30],[5,10],[15,20]],    # False
    [[7,10],[2,4]], # True
]

s = Solution()
for t in testCases:
    print(s.canAttendMeetings(t))