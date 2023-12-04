from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        def dfs(root):
            if not root:
                return -1
            depth_left = dfs(root.left) + 1
            depth_right = dfs(root.right) + 1
            if depth_left - depth_right > 1 or depth_right - depth_left > 1:
                self.ans = False

            return max(depth_left, depth_right)

        dfs(root)
        return self.ans


# 2 + helper(2) + helper(3)
tree1 = TreeNode(3, 
                 TreeNode(9, 
                          TreeNode(15), 
                          TreeNode(7)), 
                 TreeNode(20))
tree2 = TreeNode(1, 
                 TreeNode(2, 
                          TreeNode(3), 
                          TreeNode(3, 
                                   TreeNode(4), 
                                   TreeNode(4))),
                 TreeNode(2))

testCases = [
    tree1, # True
    tree2
]

s = Solution()
for t in testCases:
    print(s.isBalanced(t))