from typing import List
import bisect


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # inspired by https://www.youtube.com/watch?v=LPFhl65R7ww&t=594s&ab_channel=TusharRoy-CodingMadeSimple
        # time complexity m O(log min(n, m)): m: size of the smallest list, n: size of the largest list
        # ensure nums1 is the smallest
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # binary search to find the correct partition
        low = 0
        high = len(nums1)
        while low <= high:
            mid = (high + low) // 2
            mid2 = ((len(nums1) + len(nums2) + 1) // 2) - mid
            # protect against bad indexes
            maxLeft1 = nums1[mid - 1] if mid - 1 >= 0 else float("-inf")
            minRight1 = nums1[mid] if mid < len(nums1) else float("inf")
            maxLeft2 = nums2[mid2 - 1] if mid2 - 1 >= 0 else float("-inf")
            minRight2 = nums2[mid2] if mid2 < len(nums2) else float("inf")
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # found the match!
                if (len(nums1) + len(nums2)) % 2 == 1:  # is odd
                    return max(maxLeft1, maxLeft2)
                else:  # is even
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                # move partition to the left
                high = mid - 1
            else:
                # move partition to the right
                low = mid + 1
        return -1  # should not reach here

    def findMedianSortedArraysSlow(self, nums1: List[int], nums2: List[int]) -> float:
        # time complexity m O(log n): m: size of the smallest list, n: size of the largest list
        # add elements of smaller array to the larger
        maxLen = max(len(nums1), len(nums2))
        # ensure nums2 is the smallest
        if len(nums2) > maxLen:
            nums1, nums2 = nums2, nums1
        for n in nums2:
            bisect.insort(nums1, n)
        # take mid position (or avg of pair of mid positions) as answer
        if len(nums1) % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2] + nums1[(len(nums1) // 2) - 1]) / 2

    def findMedianSortedArraysNotSwapping(self, nums1: List[int], nums2: List[int]) -> float:
        # add elements of smaller array to the larger
        maxLen = max(len(nums1), len(nums2))
        if len(nums1) >= maxLen:
            for n in nums2:
                bisect.insort(nums1, n)
            # take mid position (or avg of pair of mid positions) as answer
            if len(nums1) % 2 == 1:
                return nums1[len(nums1) // 2]
            else:
                return (nums1[len(nums1) // 2] + nums1[(len(nums1) // 2) - 1]) / 2
        else:
            for n in nums1:
                bisect.insort(nums2, n)
            # take mid position (or avg of pair of mid positions) as answer
            if len(nums2) % 2 == 1:
                return nums2[len(nums2) // 2]
            else:
                return (nums2[len(nums2) // 2] + nums2[(len(nums2) // 2) - 1]) / 2


testCases = [
    ([2], [1, 3, 4]),
    ([3], [-2, -1]),
    ([], [2, 3]),
    ([1, 3], [2, 7]),
    ([1, 2], [3, 4]),
    ([1, 3], [2]),
    ([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25]),
    ([2], [1, 3]),
]
s = Solution()
for t in testCases:
    print(s.findMedianSortedArrays(t[0], t[1]))
