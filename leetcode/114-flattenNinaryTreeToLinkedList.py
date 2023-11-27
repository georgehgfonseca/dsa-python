from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # TODO: copied from solutions
        curr = root
        
        while curr:
            if curr.left:
                p = curr.left
                while p.right:
                    p = p.right
                    
                p.right = curr.right
                
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right


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
    print(s.flatten(t))
