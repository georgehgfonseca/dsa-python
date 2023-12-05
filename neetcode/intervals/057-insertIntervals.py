from typing import List

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def overlaps(interval1, interval2):
            contains = interval1[0] <= interval2[0] and interval2[1] <= interval1[1]
            is_contained = interval2[0] <= interval1[0] and interval1[1] <= interval2[1]
            return is_contained or contains or \
                   (interval1[0] <= interval2[0] <= interval1[1]) or (interval1[0] <= interval2[1] <= interval1[1])   

        # edge cases
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]

        # get start and end indexes of overlapping intervals
        i = 0
        merged_interval = newInterval
        overlapped_at_least_once = False
        while i < len(intervals):
            if overlaps(intervals[i], newInterval):
                # merge intervals
                merged_interval = [min(intervals[i][0], merged_interval[0]), max(intervals[i][1], merged_interval[1])]
                overlapped_at_least_once = True
            i += 1

        if not overlapped_at_least_once:
            for i in range(len(intervals)):
                if intervals[i][0] > newInterval[1]:
                    intervals.insert(i, newInterval)
                    return intervals
            return intervals.append(newInterval)


        res = []
        added_merged = False
        for i in range(len(intervals)):
            if overlaps(intervals[i], merged_interval):
                if not added_merged:
                    added_merged = True
                    res.append(merged_interval)
            else:
                res.append(intervals[i])

        return res


        # res = []
        # updated_interval = [None, None]
        # start_idx = None
        # for i in range(len(intervals) - 1):
        #     start_i = intervals[i][0]
        #     start_i2 = intervals[i + 1][0]
        #     if start_i <= newInterval[0] and start_i2 >= newInterval[0]:
        #         start_idx = i
        #         updated_interval[0] = start_i
        #         break
        #     res.append(intervals[i])


        # end_idx = None
        # for j in range(start_idx, len(intervals)):
        #     start_j = intervals[j][0]
        #     if newInterval[1] <= start_j:
        #         end_idx = j
        #         updated_interval[1] = newInterval[1]
        #         res.append(updated_interval)
        #         break

        # res += intervals[end_idx:]
        # return res


testCases = [
    ([[3,5],[12,15]], [18,19]),                       # [[1,5], [6,9]]
    ([[3,5],[12,15]], [1,2]),                       # [[1,5], [6,9]]
    ([[3,5],[12,15]], [6,6]),                       # [[1,5], [6,9]]
    ([[1,5]], [6,8]),                       # [[1,5], [6,9]]
    ([[1,3],[6,9]], [2,5]),                       # [[1,5], [6,9]]
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),  # [[1,2],[3,10],[12,16]]
]

s = Solution()
for t in testCases:
    print(s.insert(t[0], t[1]))