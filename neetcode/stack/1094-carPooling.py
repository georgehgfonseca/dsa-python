import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        endHeap = []
        currPass = 0

        for i in range(len(trips)):
            pas, start, end = trips[i]
            while endHeap and start >= endHeap[0][0]:
                currEnd, endPass = heapq.heappop(endHeap)
                currPass -= endPass

            currPass += pas
            heapq.heappush(endHeap, (end, pas))
            if currPass > capacity:
                return False

        return True