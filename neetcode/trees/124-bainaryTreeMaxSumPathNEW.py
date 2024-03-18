from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # convert tree to a graph

        # run bellman-
        pass



tree0 = TreeNode(-10, 
                 TreeNode(9), 
                 TreeNode(20, 
                          TreeNode(15),
                          TreeNode(7)))
tree1 = TreeNode(-2, 
                 TreeNode(-1), 
                 None) 
tree2 = TreeNode(3, 
                 TreeNode(1,
                          TreeNode(0),
                          TreeNode(2)), 
                 TreeNode(5, 
                          TreeNode(4),
                          TreeNode(6)))
tree3 = TreeNode(2, 
                 TreeNode(1), 
                 TreeNode(3))
tree4 = TreeNode(2, 
                 TreeNode(2), 
                 TreeNode(2))
tree5 = TreeNode(5, 
                 TreeNode(1), 
                 TreeNode(4, 
                          TreeNode(3), 
                          TreeNode(6)))

testCases = [
    tree0, 
    tree1, 
    tree2, 
    tree3, 
    tree4, 
    tree5, 
]

s = Solution()
for t in testCases:
    print(s.maxPathSum(t))
