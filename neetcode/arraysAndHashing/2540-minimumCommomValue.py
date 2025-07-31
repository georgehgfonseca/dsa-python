class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        setNums2 = set(nums2)
        for num in nums1:
            if num in setNums2:
                return num
        return -1

    def getCommonTL(self, nums1: List[int], nums2: List[int]) -> int:
        for num in nums1:
            if num in nums2:
                return num
        return -1