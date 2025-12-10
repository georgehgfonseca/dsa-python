from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        newStart, newEnd = newInterval
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if newStart > end:
                res.append(intervals[i])
                continue

            if newEnd < start:
                res.append([newStart, newEnd])
                res += intervals[i:]
                return res

            newStart = min(newStart, start)
            newEnd = max(newEnd, end)

        res.append([newStart, newEnd])

        return res
