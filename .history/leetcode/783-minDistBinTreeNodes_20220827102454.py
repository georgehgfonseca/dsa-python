from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # get array of nodes
        def helper(root: Optional[TreeNode]):
            if not root:
                return []
            return [root.val] + helper(root.left) + helper(root.right)

        arr = helper(root)
        if len(arr) < 2:
            return 0
        arr.sort()
        min = float("inf")
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[1] < min:
                min = arr[i + 1] - arr[1]
        return min

    def minDiffInBSTWA(self, root: Optional[TreeNode]) -> int:
        if root.left and root.right:
            return min(
                root.val - root.left.val,
                root.right.val - root.val,
                self.minDiffInBST(root.left),
                self.minDiffInBST(root.right),
            )
        elif root.left and not root.right:
            return min(root.val - root.left.val, self.minDiffInBST(root.left))
        elif not root.left and root.right:
            return min(root.right.val - root.val, self.minDiffInBST(root.right))
        else:
            return float("inf")


t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
testCases = [t]
s = Solution()
for t in testCases:
    print(s.minDiffInBST(t))
