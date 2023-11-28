from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        self.min_depth = float("inf")

        def helper(root, depth):
            if root:
                depth += 1
                if not root.left and not root.right:
                    if depth < self.min_depth:
                        self.min_depth = depth
                helper(root.left, depth)
                helper(root.right, depth)
        
        if not root:
            return 0
        
        helper(root, 0)
        return self.min_depth




t1 = TreeNode(3, 
             TreeNode(9), 
             TreeNode(20, 
                      TreeNode(15),
                      TreeNode(17)))
t2 = TreeNode(1, 
             TreeNode(2, 
                      TreeNode(3), 
                      TreeNode(3, 
                               TreeNode(4), 
                               TreeNode(4))), 
             TreeNode(2))

testCases = [t1, t2]
s = Solution()
for t in testCases:
    print(s.minDepth(t))
