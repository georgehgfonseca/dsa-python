from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # copied the solution (had a really hard time on this one)
        self.res = 0

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.res            

        # def helper(root):
        #     if not root.left and not root.right:
        #         # diameter of a leaf node is 0
        #         return 0
        #     if root.left and root.right:
        #         return helper(root.left) + helper(root.right) + 2
        #     elif not root.left:
        #         return helper(root.right) + 1
        #     elif not root.right:
        #         return helper(root.left) + 1

        # return helper(root)

# 2 + helper(2) + helper(3)
tree1 = TreeNode(1, 
                 TreeNode(2, 
                          TreeNode(4), 
                          TreeNode(5)), 
                 TreeNode(3))
tree2 = TreeNode(1, 
                 TreeNode(2),
                 TreeNode(3))

testCases = [
    tree1,
    tree2
]

s = Solution()
for t in testCases:
    print(s.diameterOfBinaryTree(t))