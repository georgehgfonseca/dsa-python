from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list3 = ListNode()
        head_list3 = list3

        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
                list3 = list3.next
            else:
                list3.next = list2
                list2 = list2.next
                list3 = list3.next
        
        # Handle the case when gets to the end of list1 or list2
        if not list1:
            list3.next = list2
        if not list2:
            list3.next = list1

        return head_list3.next


t1 = ListNode(1, ListNode(2, ListNode(4)))
t2 = ListNode(1, ListNode(3, ListNode(4)))

testCases = [(t1, t2)]
s = Solution()
for t in testCases:
    print(s.mergeTwoLists(t[0], t[1]))
