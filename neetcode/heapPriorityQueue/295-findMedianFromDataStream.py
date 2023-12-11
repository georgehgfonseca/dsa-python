from typing import List
import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeapLeft = []
        self.minHeapRight = []
        

    def addNum(self, num: int) -> None:
        if not self.minHeapRight:
            heapq.heappush(self.minHeapRight, num)
            return

        if num > self.minHeapRight[0]:
            heapq.heappush(self.minHeapRight, num)
        else:
            heapq.heappush(self.maxHeapLeft, -num)
        
        # balance heaps
        if len(self.minHeapRight) > len(self.maxHeapLeft) + 1:
            # pass min element of minHeap to maxHeap
            elem = heapq.heappop(self.minHeapRight)
            heapq.heappush(self.maxHeapLeft, -elem)
        if len(self.maxHeapLeft) > len(self.minHeapRight) + 1:
            # pass min element of maxHeap to minHeap
            elem = heapq.heappop(self.maxHeapLeft)
            heapq.heappush(self.minHeapRight, -elem)        

    def findMedian(self) -> float:
        size = len(self.minHeapRight) + len(self.maxHeapLeft)
        if size % 2 == 1:
            # return fisrt elem of largest heap
            if len(self.minHeapRight) > len(self.maxHeapLeft):
                return self.minHeapRight[0]
            else:
                return -self.maxHeapLeft[0]
        else:
            return (self.minHeapRight[0] + -self.maxHeapLeft[0]) / 2
        

medianFinder = MedianFinder();
medianFinder.addNum(1);    # arr = [1]
medianFinder.addNum(2);    # arr = [1, 2]
print(medianFinder.findMedian()); # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    # arr[1, 2, 3]
print(medianFinder.findMedian()); # return 2.0



heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
heapq.heappush(heap, 9)
heapq.heappush(heap, 8)
print(heap)