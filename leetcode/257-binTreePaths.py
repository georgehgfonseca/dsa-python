from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def arrToPath(arr):
            ans = str(arr[0])
            for i in range(1, len(arr)):
                ans = ans + "->" + str(arr[i])
            return ans

        def helper(root, curr, paths):
            curr.append(root.val)
            if not root.left and not root.right:
                paths.append(arrToPath(curr))
            if root.left:
                helper(root.left, curr[:], paths)
            if root.right:
                helper(root.right, curr[:], paths)

        helper(root, [], paths)
        return paths


t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
testCases = [t, t2]
s = Solution()
for t in testCases:
    print(s.binaryTreePaths(t))
