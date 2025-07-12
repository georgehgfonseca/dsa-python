from typing import Optional

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        lenght = 0
        curr = head
        while curr:
            lenght += 1
            curr = curr.next

        pos_to_remove = lenght - n

        prev = None
        curr = head
        pos = -1
        while curr:
            pos += 1
            if pos == pos_to_remove:
                if prev:
                    prev.next = curr.next
                    curr.next = None
                    return head
                else:
                    return head.next
            prev = curr
            curr = curr.next

        # could to it easier just gettin the lenght of the list and removing (len - n)th position
        # reverse the list
        # def reverseList(head):
        #     prev = None
        #     curr = head
        #     while curr:
        #         temp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = temp
        #     return prev
        
        # rev_head = reverseList(head)
        # rev_head_ref = rev_head

        # prev = None
        # next_pos = 0
        # while rev_head:
        #     if next_pos == n-1:
        #         if prev:
        #             prev.next = rev_head.next
        #             rev_head.next = None
        #         else:
        #             rev_head_ref = rev_head.next
        #         break
        #     prev = rev_head
        #     rev_head = rev_head.next
        #     next_pos += 1

        # final = reverseList(rev_head_ref)

        # return final

testCases = [
    # ((ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), 2),
    # (ListNode(1), 1),
    (ListNode(1, ListNode(2)), 1),
]

s = Solution()
for t in testCases:
    print(s.removeNthFromEnd(t[0], t[1]))