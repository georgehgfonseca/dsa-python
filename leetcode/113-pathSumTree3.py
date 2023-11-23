from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        if not root:
            return paths

        def helper(root, curr, sum, paths):
            curr.append(root.val)
            sum += root.val
            if not root.left and not root.right and sum == targetSum:
                paths.append(curr)
            if root.left:
                helper(root.left, curr[:], sum, paths)
            if root.right:
                helper(root.right, curr[:], sum, paths)

        helper(root, [], 0, paths)
        return paths


t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
testCases = [(t, 8), (t2, 10)]
s = Solution()
for t in testCases:
    print(s.pathSum(t[0], t[1]))
