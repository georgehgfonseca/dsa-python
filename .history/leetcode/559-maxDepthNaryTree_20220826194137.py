from typing import Optional

# Definition for a binary tree node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        def helper(root: "Node", depth: int):
            if root == None or root.children == None:
                return depth
            else:
                childDepths = []
                for child in root.children:
                    childDepths.append(helper(child, depth + 1))
                return max(childDepths)

        depth = 0
        return helper(root, depth)


t = Node(1, [Node(2), Node(3, [Node(5), Node(6)]), Node(4)])
testCases = [t]
s = Solution()
for t in testCases:
    print(s.maxDepth(t))
