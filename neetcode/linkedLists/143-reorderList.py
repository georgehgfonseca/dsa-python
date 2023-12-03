from typing import Optional

class Node:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[Node]) -> None:
        # need to see the idea on video and fix details in code with answer

        # obtain a pointer to the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        curr = slow.next
        prev = slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge two halfs
        start, end = head, prev
        while end:
            tmp1, tmp2 = start.next, end.next
            start.next = end
            end.next = tmp1
            start, end = tmp1, tmp2


testCases = [
    Node(1, Node(2, Node(3, Node(4))))
]

s = Solution()
for t in testCases:
    print(s.reorderList(t))