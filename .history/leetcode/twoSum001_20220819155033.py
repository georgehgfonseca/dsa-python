from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # Runs in O(n)
    comp = {}
    for i in range(len(nums)):
        if nums[i] not in comp:
            comp[nums[i]] = i
        if target - nums[i] in comp and i != comp[target - nums[i]]:
            return [i, comp[target - nums[i]]]


def twoSumSlow(nums: List[int], target: int) -> List[int]:
    # Runs in O(n^2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


t1 = ([2, 7, 11, 15], 9)
t2 = ([3, 2, 4], 6)
t3 = ([3, 3], 6)
testCases = [t1, t2, t3]
for t in testCases:
    print(twoSum(t[0], t[1]))
