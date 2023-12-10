from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = cur = ListNode()

        offset = 0
        while l1 or l2 or offset:
            sum = offset
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val
            digit = sum % 10
            offset = sum // 10

            cur.next = ListNode(digit)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return l3.next


testCases = [
    (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
]

s = Solution()
for t in testCases:
    print(s.addTwoNumbers(t[0], t[1]))