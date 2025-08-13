# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        i = 1
        curr = head
        tail = dummy
        while i < left and curr:
            tail = curr
            curr = curr.next
            i += 1

        # reverse sublist
        prev = ListNode()
        subListTail = curr
        while i <= right and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1
        
        tail.next = prev
        subListTail.next = curr
        return dummy.next

        
