# Definition for singly-linked list.
from typing import List, Optional
import bisect
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time complexity O(n log m): n total of elements in lists; m num of lists
        # space complexity O(m)
        if not lists:
            return None
        # create priority queue
        pq = []
        heapq.heapify(pq)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, [lists[i].val, i])

        head = ListNode(-1)  # dummy value
        ans = head
        while pq:
            [minVal, minI] = heapq.heappop(pq)
            # change pointer and move to next
            head.next = lists[minI]
            head = head.next
            if lists[minI].next:
                lists[minI] = lists[minI].next
                heapq.heappush(pq, [lists[minI].val, minI])
        return ans.next

    def mergeKListsSlow(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time complexity O(n * m): n total of elements in lists; m num of lists
        # space complexity O(1)
        if not lists:
            return None
        head = ListNode(-1)  # dummy value
        ans = head
        while True:
            minVal = float("inf")
            minI = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < minVal:
                    minVal = lists[i].val
                    minI = i
            if minI == -1:
                break
            # change pointer and move to next
            head.next = lists[minI]
            head = head.next
            if lists[minI].next:
                lists[minI] = lists[minI].next
            else:
                lists.pop(minI)
        return ans.next

    def mergeKListsArray(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # space complexity O(n) n: total of elements in lists
        # time complexity O(n log n): bottleneck is sorting the array
        if not lists:
            return None
        # preprocessing convert into arrays (is it allowed?)
        arr = []
        overallSize = 0
        for l in range(len(lists)):
            head = lists[l]
            if head:
                while head:
                    bisect.insort(arr, head.val)  # arr.append(head.val)
                    head = head.next
                    overallSize += 1
        # sort arr
        # arr.sort() # no need to sort if inserted in order
        # convert into ListNode
        head = ListNode(-1)  # dummy value
        ans = head
        for i in range(len(arr)):
            newNode = ListNode(arr[i])
            head.next = newNode
            head = head.next
        return ans.next


testCases = [[ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]]
s = Solution()
for t in testCases:
    print(s.mergeKLists(t))
