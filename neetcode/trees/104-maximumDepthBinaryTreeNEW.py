from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root, depth):
            if not root:
                return depth

            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))

        return dfs(root, 0)





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