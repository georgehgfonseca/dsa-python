from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []

        def helper(root: Optional[TreeNode], to_delete: List[int], ans: List[Optional[TreeNode]]):
            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
            pass

        return helper(root, to_delete, ans)


t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
testCases = [t]
s = Solution()
for t in testCases:
    print(s.delNodes(t))
