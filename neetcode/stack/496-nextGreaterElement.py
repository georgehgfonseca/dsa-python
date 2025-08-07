class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2         = [4, 3, 2, 5, 6, 1, 7]
        # i             =  *
        # pending       = [3]
        # numLarger     = {}
        pending = []
        numLarger = dict()
        for i in range(len(nums2)):
            while pending and nums2[i] > pending[-1]:
                num = pending.pop()
                numLarger[num] = nums2[i]
            pending.append(nums2[i])

        res = []
        for num in nums1:
            if num in numLarger:
                res.append(numLarger[num])
            else:
                res.append(-1)
        return res