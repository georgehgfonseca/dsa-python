from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], depth: int):
            if root == None:
                return depth
            else:
                return max(helper(root.left, depth + 1), helper(root.right, depth + 1))

        depth = 0
        return helper(root, depth)


t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))  # [1,2,2,3,4,4,3]
t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))  # [1,2,2,null,3,null,3]
testCases = [t2]
s = Solution()
for t in testCases:
    print(s.maxDepth(t))
