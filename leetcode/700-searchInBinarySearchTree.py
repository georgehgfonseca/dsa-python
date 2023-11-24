from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val == val:
                return root
            if val < root.val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)
            


t = (TreeNode(4, 
             TreeNode(2, 
                      TreeNode(1), 
                      TreeNode(3)), 
             TreeNode(7)), 2)

testCases = [t]
s = Solution()
for t in testCases:
    print(s.searchBST(t[0], t[1]))
