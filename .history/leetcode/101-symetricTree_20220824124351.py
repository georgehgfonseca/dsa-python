from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]):
            if root.left == None and root.right == None:
                return True
            if root.left == root.right:
                return helper(root.left) and helper(root.right)
            else:
                return False

        return helper(root)


testCases = [([1, 2, 2, 3, 4, 4, 3])]
s = Solution()
for t in testCases:
    print(s.isSymmetric(t))
