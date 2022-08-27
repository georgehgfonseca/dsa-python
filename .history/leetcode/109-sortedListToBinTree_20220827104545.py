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
        # convert to array (is it allowed?)
        def toArray(head):
            return [head.val] + toArray(head.next)

        arr = toArray(head)

        # find root element (mid element of input arr/list)
        def insertInBST(root, val):
            if root.val >= val:
                root.left

        currIdx = len(arr) // 2
        rootVal = arr[currIdx]
        root = TreeNode(rootVal)


testCases = [ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))]
s = Solution()
for t in testCases:
    print(s.sortedListToBST(t))
