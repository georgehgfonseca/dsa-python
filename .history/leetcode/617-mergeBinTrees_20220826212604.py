from typing import Optional

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
        def helper(root1: Optional[Node], root2: Optional[Node]):
            if root1.left and root2.left:
                return helper(root1.left, root2.left)
            elif root1.left and not root2.left:
                return root1.left
            elif not root1.left and root2.left:
                return root2.left
            else:
                return

                if root1.left and root2.left:
                    helper(root1.left, root2.left)

        merged = root1
        return helper(root1, root2)


t = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))  # [1,2,2,3,4,4,3]
t2 = Node(1, Node(2, None, Node(3)), Node(2, None, Node(3)))  # [1,2,2,null,3,null,3]
t3 = Node(1, Node(3, Node(5), None), Node(2, None, None))
t4 = Node(2, Node(1, None, Node(4)), Node(3, None, Node(7)))
testCases = [(t3, t4), (t, t2)]
s = Solution()
for t in testCases:
    print(s.mergeTrees(t))
