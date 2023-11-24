# Definition for singly-linked list.
from typing import List, Optional
import bisect
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        list3_head_ref = list3
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

        if list1 and not list2:
            list3.next = list1
        if list2 and not list1:
            list3.next = list2

        return list3_head_ref.next





t1 = (ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))))
testCases = [t1]
s = Solution()
for t in testCases:
    print(s.mergeTwoLists(t[0], t[1]))
