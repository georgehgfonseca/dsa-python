from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
testCases = [t]
s = Solution()
for t in testCases:
    print(s.minDiffInBST(t))
