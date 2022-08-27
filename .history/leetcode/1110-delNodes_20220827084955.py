from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToArray(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def helper(root: Optional[TreeNode]) -> List[int]:
            if root:
                ans.append(root.val)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

        helper(root)
        return ans

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = [root]

        def helper(
            root: Optional[TreeNode], del_node: int, ans: List[Optional[TreeNode]], t: int, rootRef: Optional[TreeNode]
        ) -> bool:
            if root.val == del_node:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                root = None
                ans[t] = rootRef
                return True
            if root.left:
                helper(root.left, del_node, ans, t, rootRef)
            if root.right:
                helper(root.right, del_node, ans, t, rootRef)
            return False

        for i in range(len(to_delete)):
            # delete i from each tree in ans (probably only one)
            for t in range(len(ans)):
                if helper(ans[t], to_delete[i], ans, t, ans[t]):
                    break
        for a in ans:
            self.treeToArray(a)

        return ans


t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
testCases = [(t, [3, 5])]
s = Solution()
for t in testCases:
    print(s.delNodes(t[0], t[1]))
