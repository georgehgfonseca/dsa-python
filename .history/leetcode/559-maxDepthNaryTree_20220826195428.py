from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        def helper(root: "Node", depth: int):
            if root == None:
                return depth
            if root.children == None or len(root.children) == 0:
                return depth + 1
            else:
                return max([helper(child, depth + 1) for child in root.children])

        depth = 0
        return helper(root, depth)

    # # cleaner code (from the web)
    # def maxDepth(self, root: "Node") -> int:
    #     if root == None:
    #         return 0
    #     if len(root.children) == 0:
    #         return 1
    #     return max([self.maxDepth(child) for child in root.children]) + 1


t = Node(1, [Node(2), Node(3, [Node(5), Node(6)]), Node(4)])
t2 = Node(
    1,
    [
        Node(2),
        Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
        Node(4, [Node(8, [Node(12)])]),
        Node(5, [Node(9, [Node(13)]), Node(10)]),
    ],
)
testCases = [t, t2]
s = Solution()
for t in testCases:
    print(s.maxDepth(t))
