from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def helper(root, val):
            if val <= root.val:
                if root.left:
                    helper(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    helper(root.right, val)
                else:
                    root.right = TreeNode(val)

        if not root:
            return TreeNode(val)

        helper(root, val)
        return root 
            


t = (TreeNode(4, 
             TreeNode(2, 
                      TreeNode(1), 
                      TreeNode(3)), 
             TreeNode(7)), 5)

testCases = [t]
s = Solution()
for t in testCases:
    print(s.insertIntoBST(t[0], t[1]))
