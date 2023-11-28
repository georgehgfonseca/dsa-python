from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        # self.count = 0
        # def helper(root):
        #     if root:
        #         self.count += 1
        #         helper(root.left)
        #         helper(root.right)
        
        # helper(root)
        # return self.count


t1 = TreeNode(1, 
              TreeNode(3,
                       TreeNode(5),
                       None), 
              TreeNode(2))
t2 = TreeNode(2, 
              TreeNode(1,
                       None,
                       TreeNode(4)), 
              TreeNode(3,
                       None,
                       TreeNode(7, 
                                None,
                                None)))

testCases = [t1, t2]
s = Solution()
for t in testCases:
    print(s.countNodes(t))
