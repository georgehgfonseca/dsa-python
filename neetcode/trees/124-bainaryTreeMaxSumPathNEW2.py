from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(root):
            if not root.left and not root.right:
                self.res = max(self.res, root.val)
                return root.val
            
            leftSum = dfs(root.left) if root.left else 0
            rightSum = dfs(root.right) if root.right else 0
            nodeSum = max(root.val, root.val + leftSum + rightSum, root.val + leftSum, root.val + rightSum)
            self.res = max(self.res, nodeSum)
            return max(root.val, root.val + leftSum, root.val + rightSum)
        
        dfs(root)
        return self.res


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
tree4 = TreeNode(1, 
                 TreeNode(-2), 
                 TreeNode(3))
tree5 = TreeNode(5, 
                 TreeNode(1), 
                 TreeNode(4, 
                          TreeNode(3), 
                          TreeNode(6)))
tree6 = TreeNode(-15, 
                 TreeNode(10), 
                 TreeNode(20, 
                          TreeNode(15,
                                   TreeNode(-5),
                                   None), 
                          TreeNode(5)))
tree7 = TreeNode(5, 
                 TreeNode(4,
                          TreeNode(11,
                                   TreeNode(7),
                                   TreeNode(2))), 
                 TreeNode(8, 
                          TreeNode(13), 
                          TreeNode(4,
                                   None,
                                   TreeNode(1))))

testCases = [
    # tree0, 
    # tree1, 
    # tree2, 
    # tree3, 
    # tree4, 
    # tree5, 
    # tree6, 
    tree7, 
]

s = Solution()
for t in testCases:
    print(s.maxPathSum(t))
