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
        # get array of nodes
        def helper(root: Optional[TreeNode]):
            if not root:
                return []
            return helper(root.left) + [root.val] + helper(root.right)

        # find min diff
        arr = helper(root)
        if len(arr) < 2:
            return 0
        # arr.sort() (not needed if arr is in preorder)
        min = float("inf")
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < min:
                min = arr[i + 1] - arr[i]
        return min


t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
testCases = [ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))]
s = Solution()
for t in testCases:
    print(s.sortedListToBST(t))
