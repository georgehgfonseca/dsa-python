class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        for i in range(len(nums) + 1):
            if i not in numsSet:
                return i

    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(1, len(nums) + 1):
            total += i
        return total - sum(nums)
        
    def missingNumber(self, nums: List[int]) -> int:
        # TODO: bitwise XOR (didn't get it)
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr

        