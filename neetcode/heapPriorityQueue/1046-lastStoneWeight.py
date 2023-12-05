from typing import List
import heapq

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:

        # transform values so that I can keep using a minPQueue
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                res = stone1 - stone2
                heapq.heappush(stones, res)
        
        if not stones:
            return 0
        return -stones[0]

testCases = [
    [2,7,4,1,8,1],  # [1,1,2,4,7,8] -> [1,1,1,2,4] -> [1,1,1,2] -> [1,1,1] -> [1] 1
    [2,7,4,1,8,1],  # [-8,-7,-4,-2,-1,-1] -> [-4,-2,-1,-1,-1] -> [-2,-1,-1,-1] -> [-1,-1,-1] -> [-1] 1
]

s = Solution()
for t in testCases:
    print(s.lastStoneWeight(t))