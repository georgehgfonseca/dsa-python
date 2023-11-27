from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def helper(root):
            if not root:
                return []            
            return helper(root.left) + [root.val] + helper(root.right)

        return helper(root)



t = TreeNode(1, 
             TreeNode(2, 
                      TreeNode(4), 
                      TreeNode(5)), 
             TreeNode(3, 
                      TreeNode(6), 
                      TreeNode(7)))
testCases = [t]
s = Solution()
for t in testCases:
    print(s.inorderTraversal(t))
