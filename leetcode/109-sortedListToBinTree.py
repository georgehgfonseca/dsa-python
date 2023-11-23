from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def insertNode(arr):
            if arr:
                return TreeNode(
                    arr[len(arr) // 2],
                    insertNode(arr[: len(arr) // 2]),
                    insertNode(arr[(len(arr) // 2) + 1 :]),
                )

        return insertNode(arr)


testCases = [ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))]
s = Solution()
for t in testCases:
    print(s.sortedListToBST(t))
