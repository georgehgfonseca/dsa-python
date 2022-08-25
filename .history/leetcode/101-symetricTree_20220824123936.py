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


testCases = [4, 8, 1, 16, 10, 0]
s = Solution()
for t in testCases:
    print(s.mySqrt(t))
