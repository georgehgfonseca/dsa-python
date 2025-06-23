from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # meetings      = [[1,20],[2,10],[3,5],[4,9],[6,8]]
        # roomEnd       = [20, 10, 5]
        # roomAssign    = [1, 1, 1]
        # smalestEnd    = 5
        # smalestIdx    = 2
        # delay         =
        # when a meeting cannot be started, decrease all end times by the min(difference)
        # delayed equals to decreasing the time for the other rooms
        # sort the meetings
        meetings.sort()
        roomEnd = [0 for _ in range(n)]
        roomAssignments = [0 for _ in range(n)]
        for meeting in meetings:
            assigned = False
            smallestEnd = float("inf")
            smallestIdx = -1
            for i in range(len(roomEnd)):  # optimize with priority queue
                if meeting[0] >= roomEnd[i]:
                    # room is available - assign the room
                    roomEnd[i] = meeting[1]
                    roomAssignments[i] += 1
                    assigned = True
                    break
                if roomEnd[i] < smallestEnd:
                    smallestEnd = roomEnd[i]
                    smallestIdx = i
            if not assigned:
                # "delay" the meeting and assign to the smallestEnd
                delay = smallestEnd - meeting[0]
                delayedMeeting = [meeting[0] + delay, meeting[1] + delay]
                roomEnd[smallestIdx] = delayedMeeting[1]
                roomAssignments[smallestIdx] += 1

        # get the room with most assignemnts
        maxAssignments = roomAssignments[0]
        maxIdx = 0
        print(roomEnd)
        print(roomAssignments)
        for i in range(1, len(roomAssignments)):
            if roomAssignments[i] > maxAssignments:
                maxAssignments = roomAssignments[i]
                maxIdx = i
        return maxIdx

    def mostBookedPQ(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]  # Min heap for available rooms
        used = []  # Min heap for used rooms [(end_time, room_number)]
        count = [0] * n  # Count of meetings for each room

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))


testCases = [
    [[0, 30], [5, 10], [15, 20]],
    [[7, 10], [2, 4]],
]

s = Solution()
for t in testCases:
    print(s.meetingRooms(t))
