from typing import Optional

class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution():

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Had to look the video AND see the solution
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
        # recursive solution
        # if not head:
        #     return None
        
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead



testCases = [
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
]
s = Solution()
for t in testCases:
    print(s.reverseList(t))