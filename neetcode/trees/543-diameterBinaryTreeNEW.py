from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        self.diameter = 0
        def helper(root):
            if not root:
                return
            
            currDiameter = height(root.left) + height(root.right)
            self.diameter = max(self.diameter, currDiameter)

            helper(root.left)
            helper(root.right)

        helper(root)

        return self.diameter
  
# root=[1,null,2,3,4,5]
tree0 = TreeNode(1,
                 None, 
                 TreeNode(2, 
                          TreeNode(3,
                                   TreeNode(5),
                                   None), 
                          TreeNode(4)))
tree1 = TreeNode(1, 
                 TreeNode(2, 
                          TreeNode(4), 
                          TreeNode(5)), 
                 TreeNode(3))
tree2 = TreeNode(1, 
                 TreeNode(2),
                 TreeNode(3))

testCases = [
    tree0,
    tree1,
    tree2
]

s = Solution()
for t in testCases:
    print(s.diameterOfBinaryTree(t))