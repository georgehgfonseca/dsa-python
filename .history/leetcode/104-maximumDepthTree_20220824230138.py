from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left == None and right == None:
                return True
            if (left == None and right != None) or (left != None and right == None):
                return False
            if left.val == right.val:
                return helper(left.left, right.right) and helper(left.right, right.left)
            else:
                return False

        return helper(root.left, root.right)


t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))  # [1,2,2,3,4,4,3]
t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))  # [1,2,2,null,3,null,3]
testCases = [t2]
s = Solution()
for t in testCases:
    print(s.isSymmetric(t))
