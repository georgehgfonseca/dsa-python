from typing import Optional

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
        def helper(root: Optional[Node], depth: int):
            if root == None:
                return depth
            else:
                return max(helper(root.left, depth + 1), helper(root.right, depth + 1))

        depth = 0
        return helper(root, depth)


t = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))  # [1,2,2,3,4,4,3]
t2 = Node(1, Node(2, None, Node(3)), Node(2, None, Node(3)))  # [1,2,2,null,3,null,3]
t3 = Node(1, Node(3, Node(5), None), Node(2, None, None))
t4 = Node(2, Node(1, None, Node(4)), Node(3, None, Node(7)))
testCases = [(t3, t4), (t, t2)]
s = Solution()
for t in testCases:
    print(s.maxDepth(t))
