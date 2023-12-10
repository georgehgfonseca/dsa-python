from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        idx_node = {}
        node_idx = {}
        i = -1
        while curr:
            i += 1
            idx_node[i] = curr
            node_idx[curr] = i
            curr = curr.next

        # create new list
        curr = head
        def helper(curr):
            if curr:
                return Node(curr.val, helper(curr.next))
        
        # map each index with its node
        copy_idx_node = {}
        curr = copy_head = helper(curr)
        i = -1
        while curr:
            i += 1
            copy_idx_node[i] = curr
            curr = curr.next

        # # fix random pointer
        curr = copy_head
        i = -1
        while curr:
            i += 1
            random = idx_node[i].random
            if random:
                random_idx = node_idx[random]
                curr.random = copy_idx_node[random_idx]
            curr = curr.next

        return copy_head


node5 = Node(1, None)
node4 = Node(10, node5)
node3 = Node(11, node4)
node2 = Node(13, node3)
node1 = Node(7, node2)

node5.random = node1
node4.random = node3
node3.random = node5
node2.random = node1
node1.random = None

node13 = Node(3, None)
node12 = Node(3, node13)
node11 = Node(3, node12)

node13.random = None
node12.random = node11
node11.random = None

testCases = [
    node1,
    node11,
]

s = Solution()
for t in testCases:
    print(s.copyRandomList(t))