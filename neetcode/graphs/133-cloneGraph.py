from typing import List, Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # had to look the solution at neetcode
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None        

        # node_clone = dict()
        # self.clone_ref = None

        # def dfs(node, neighbor):
        #         # first node being copied
        #     if neighbor.val not in node_clone:
        #         newNode = Node(neighbor.val)
        #         node_clone[neighbor] = newNode
        #         if not node: 
        #             self.clone_ref = newNode
        #         if node:
        #             node_clone[node].neighbors.append(newNode)
        #             newNode.neighbors.append(node_clone[node])
        #         for nei_neighbohor in neighbor.neighbors:
        #             if nei_neighbohor not in node_clone:
        #                 dfs(neighbor, nei_neighbohor)

        # if not node:
        #     return None
        # dfs(None, node)

        # return self.clone_ref


        # idx_node = {}
        # node_idx = {}
        # copy = []

        # # store maps for index-node and vice-versa
        # for i in range(len(node)):
        #     idx_node[i] = node[i]
        #     node_idx[node[i]] = i
        #     newNode = Node(node[i].val)
        #     copy.append(newNode)

        # # fill copy with neighborhood relations
        # for i in range(len(node)):
        #     for neighbor in node[i].neighbors:
        #         neighbor_index = node_idx[neighbor]
        #         copy[i].neighbors.append(copy[neighbor_index])

        # return copy


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

testCases = [
    node1
]

s = Solution()
for t in testCases:
    print(s.cloneGraph(t))