from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Without converting to array
        # Get list length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # self.head = head

        def make_tree(head, start, end):
            
            if start > end:
                return None
            
            mid = (start + end) // 2
            left = make_tree(head, start, mid-1)          
            root = TreeNode(head.val)
            head = head.next
            root.left=left
            
            root.right=make_tree(head, mid + 1, end)
            return root
        
        return make_tree(head, 0,n-1)
    
        # # Get array from list
        # arr = []
        # temp = head
        # while(temp):
        #     arr.append(temp.val)
        #     temp = temp.next

        # def helper(arr):
        #     if arr:
        #         mid = (len(arr) - 1) // 2
        #         return TreeNode(arr[mid], helper(arr[0:mid]), helper(arr[mid + 1:])) 

        # return helper(arr)

t1 = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
testCases = [t1]
s = Solution()
for t in testCases:
    print(s.sortedListToBST(t))
