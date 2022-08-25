from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return False


testCases = [([1, 2, 2, 3, 4, 4, 3])]
s = Solution()
for t in testCases:
    print(s.mySqrt(t))
