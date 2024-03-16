from typing import Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return helper(p.left, q.left) and helper(p.right, q.right)
            else:
                return False
            
        return helper(p, q)

t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(3))
t3 = TreeNode(1, TreeNode(2), None)
t4 = TreeNode(1, None, TreeNode(2))

testCases = [(t1, t2), (t3, t4)]

s = Solution()
for t in testCases:
    print(s.isSameTree(t[0], t[1]))