from typing import List
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # from neetcode
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

    def leastIntervalWA(self, tasks: List[str], n: int) -> int:
        # wrong answer
        
        # map task to its occurency count
        task_times = dict()
        for task in tasks:
            if task not in task_times:
                task_times[task] = 0
            task_times[task] += 1

        # keep a heapq based on task's cooldown time
        cooldown_heap = [[1, task] for task in task_times]

        interval_count = 0

        while cooldown_heap:
            interval_count += 1

            # decrease all cooldowns by 1
            for i in range(len(cooldown_heap)):
                if cooldown_heap[i][0] != 0:
                    cooldown_heap[i][0] -= 1

            cooldown, task = heapq.heappop(cooldown_heap)

            # idle interval (cannot process nearest task)
            if cooldown != 0:
                heapq.heappush(cooldown_heap, [cooldown, task])
                continue

            # remove task from task times
            task_times[task] -= 1

            # add it back to the heapq if there is more of it to run
            if task_times[task] != 0:
                heapq.heappush(cooldown_heap, [n + 1, task])

        return interval_count
        

testCases = [
    (["A","A","A","A","A","A","B","C","D","E","F","G"], 1),
    (["A","A","A","B","B","B"], 2),
]

s = Solution()
for t in testCases:
    print(s.leastInterval(t[0], t[1]))