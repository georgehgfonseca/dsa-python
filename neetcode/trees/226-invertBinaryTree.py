from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(root):
            if root:
                return TreeNode(root.val, helper(root.right), helper(root.left))
            
        return helper(root)


# root:  4
# left:  2
# right: 7

# (4, 
#     (7, 
#           (9), 
#           (6)), 
#     (2, 
#           (3), 
#           (1)))
tree1 = TreeNode(4, 
                 TreeNode(2, 
                          TreeNode(1), 
                          TreeNode(3)), 
                 TreeNode(7, 
                          TreeNode(6), 
                          TreeNode(9)))

testCases = [
    tree1
]

s = Solution()
for t in testCases:
    print(s.invertTree(t))