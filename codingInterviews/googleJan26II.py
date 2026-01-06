# buinding 4 elevators, control hallway
# 3 in maintenance
# [0 1 ... 9]
# goal? 10 - 1

# t1 -> 0 --> 9
# t2 -> 1 --> 8
# t3 -> nextStop()
# t4 -> 7 --> 6
# t5 nextStop()

# nextStop(floors: int, currPos: int, request: Tuple(int)): -> next stop

# nextStop(10, 5, (0, 5)) -> 0
# nextStop(10, 0, (0, 5)) -> 5

# nextStop(): int
# schedule(currentPosition, targetFloor)

def nextStop(floors: int, currPos: int, request: Tuple(int)):
  # todo: validate inputs
  if currPos == request[0]:
    return request[1]
  return request[0]

# 0 -> 9 (0 - 9) going up
# schedule(0, 9, [(1, 8), (5, 7), (8, 2), (3, 9)]) -> [1, 3, 5, 7, 8, 9, 8, 2]

# sort from asc
# schedule(0, 9, [(1, 8), (3, 9), (5, 7), (8, 2)]) -> [1, 3, 5, 7, 8, 9, 8, 2]
# minHeap to track where is the next stop

# TODO
# schedule(9, 0, [(1, 8), (3, 9),(5, 7), (8, 2)]) -> [1, 3, 5, 5, 7, 8, 9, 8, 2]


# nextStop() -> 0
# nextStop() -> 1
# nextStop() -> 3

# from atomic to dinamic
# handleNewRequest(5, 6) ->
# 

from collections import heapq

class Elevator:
  def __init__(self, ):
    # TODO
    self.requests = []
    self.currPos = 0
    self.floors = 0

  def handleNewRequest(curr, target):
    self.requests.append((curr, target))
    self.schedule()
  
  def schedule():
    # define targetFloor
    upwards = True if targetFloor > currPos else False
    requests.sort(reverse= not upwards)
    heap = []
    res = []

    for (start, end) in requests:
      if not heap or start > heap[0]:
        # picking up
        heapq.heappush(heap, end)
        if not res or start != res[-1]:
          res.append(start)
      else:
        while heap and start <= heap[0]:
          # delivering people
          pos = heapq.heappop(heap)
          if pos != res[-1]:
            res.append(pos)

    return res
  
