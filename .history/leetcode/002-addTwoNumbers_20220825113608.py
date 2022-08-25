from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while l1.next != None or l2.next != None:

        return None


testCases = [
    (ListNode(0), ListNode(0)),
    (
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
    ),
]
s = Solution()
for t in testCases:
    print(s.addTwoNumbers(t[0], t[1]))
