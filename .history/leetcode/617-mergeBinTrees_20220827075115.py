from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

    def mergeTreesNewTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        return TreeNode(
            root1.val + root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right)
        )

    def mergeTreesWithHelper(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if not root1:
                return root2
            if not root2:
                return root1
            return TreeNode(root1.val + root2.val, helper(root1.left, root2.left), helper(root1.right, root2.right))

        return helper(root1, root2)


t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))  # [1,2,2,3,4,4,3]
t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))  # [1,2,2,null,3,null,3]
t3 = TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2, None, None))
t4 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
testCases = [(t3, t4), (t, t2)]
s = Solution()
for t in testCases:
    print(s.mergeTrees(t[0], t[1]))
