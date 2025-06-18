from typing import List

class Solution:

    def meetingRooms(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        added_interval = [False for _ in intervals]
        res = []
        for i in range(len(intervals)):
            if not added_interval[i]:
                res.append([intervals[i]])
                for j in range(i + 1, len(intervals)):
                    lastest_interval = res[-1][-1]
                    if not added_interval[j] and lastest_interval[1] <= intervals[j][0]:
                        # can be scheduled together
                        res[-1].append(intervals[j])
                        added_interval[j] = True
        return len(res)
    
testCases = [
    [[25,579],[218,918],[623,1320],[685,1353],[1281,1307],[1308,1358]], # 3
    [[0,40],[5,10],[15,20]],    # 2
    [[0,30],[5,10],[15,20]],    # 2
    [[7,10],[2,4]], # 1
]

s = Solution()
for t in testCases:
    print(s.meetingRooms(t))