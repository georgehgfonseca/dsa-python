from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.max_depth = 0
        def helper(root, depth):
            if not root.left and not root.right:
                print(root.val, depth)
                self.max_depth = max(self.max_depth, depth)

            depth += 1
            if root.left:
                helper(root.left, depth)
            if root.right:
                helper(root.right, depth)

        if not root:
            return 0
            
        helper(root, 1)
        return self.max_depth


tree1 = TreeNode(3, 
                 TreeNode(9), 
                 TreeNode(20, 
                          TreeNode(15), 
                          TreeNode(7)))

testCases = [
    tree1
]

s = Solution()
for t in testCases:
    print(s.maxDepth(t))