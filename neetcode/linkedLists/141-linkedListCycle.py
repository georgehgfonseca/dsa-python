from typing import Optional

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while head:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False


node4 = ListNode(4, None)
node3 = ListNode(0, node4)
node2 = ListNode(2, node3)
node1 = ListNode(3, node2)
node4.next = node2

testCases = [
    node1
]

s = Solution()
for t in testCases:
    print(s.hasCycle(t))