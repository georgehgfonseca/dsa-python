from typing import List
import unittest


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas     = [1, 2, 3, 4]
        # cost    = [2, 2, 4, 1]
        # start   = 0 will always be the one with more gas?
        # pos     = 0
        # currGas = 1
        # ans     = 0
        # brute force O(n^2)
        for start in range(len(gas)):
            if gas[start] < cost[start]:
                continue
            gasStart = gas[start:] + gas[:start] + [gas[start]]
            costStart = cost[start:] + cost[:start] + [cost[start]]
            currGas = gasStart[0]
            hasCompleted = True
            for i in range(1, len(gasStart)):
                currGas -= costStart[i - 1]
                if currGas < 0:
                    hasCompleted = False
                    break
                currGas += gasStart[i]
            if hasCompleted:
                return start
        return -1


testCases = [
    (([1, 2, 3], [2, 3, 2]), -10),  # -1
    (([1, 2, 3, 4], [2, 2, 4, 1]), 3),  # -1
]

s = Solution()
for t in testCases:
    try:
        assert s.canCompleteCircuit(t[0][0], t[0][1]) == t[1]
    except AssertionError:
        print(f"Test case {t[0]} == {t[1]} failed")
