from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        def helper(root, depth):
            if root:
                if depth + 1 > self.ans:
                    self.ans = depth + 1
                helper(root.left, depth + 1)
                helper(root.right, depth + 1)

        helper(root, 0)
        return self.ans
    
        # def helper(root, depth, ans):
        #     if root:
        #         if depth + 1 > ans[0]:
        #             ans[0] = depth + 1
        #         helper(root.left, depth + 1, ans)
        #         helper(root.right, depth + 1, ans)

        # ans = [0]
        # helper(root, 0, ans)
        # return ans[0]


t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))  # [1,2,2,3,4,4,3]
t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))  # [1,2,2,null,3,null,3]
testCases = [t, t2]
s = Solution()
for t in testCases:
    print(s.maxDepth(t))
