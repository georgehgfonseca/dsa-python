from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(p, q):
            if p and q:
                return p.val == q.val and helper(p.left, q.left) and helper(p.right, q.right)
            if not p and not q:
                return True
            return False

        return helper(p, q)


t1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))  # [1,2,2,3,4,4,3]
t2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))  # [1,2,2,null,3,null,3]
t3 = TreeNode(1, 
              TreeNode(2), 
              TreeNode(3))
t4 = TreeNode(1, 
              TreeNode(2), 
              TreeNode(3))
testCases = [(t1, t2), (t3, t4)]
s = Solution()
for t in testCases:
    print(s.isSameTree(t[0], t[1]))
