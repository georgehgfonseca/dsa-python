from typing import List

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        # Had to watch the video
        # Floyd's algorithm
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break

        return slow


test_cases = [
    [1, 3, 4, 2, 2]
    # ListNode(1, ListNode(3, ListNode(4, ListNode(2, ListNode(2)))))
]

s = Solution()

for t in test_cases:
    print(s.findDuplicate(t))