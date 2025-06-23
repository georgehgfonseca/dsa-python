from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        # keep a hashset of previous numbers and another hashset of next numbers
        prev = set()
        next = set()
        for num in nums:
            prev.add(num - 1)
            next.add(num + 1)

        ans = 0
        # mark each number as processed whenever it appears on a sequence to avoid repeated work
        checked = set()
        # for each number, try to extend the sequence with prevous and next hashsets
        for i in range(len(nums)):
            if nums[i] in checked:
                continue
            checked.add(nums[i])
            currSeqLen = 1
            # expand to smaller
            currNext = nums[i]
            while currNext in prev:
                checked.add(currNext)
                prev.remove(currNext)
                currSeqLen += 1
                currNext += 1
                if currNext in checked:
                    break
            # expand to larger
            currPrev = nums[i]
            while currPrev in next:
                checked.add(currPrev)
                currSeqLen += 1
                next.remove(currPrev)
                currPrev -= 1
                if currPrev in checked:
                    break

            ans = max(ans, currSeqLen)
        return ans

        if len(nums) in [0, 1]:
            return len(nums)
        nums = list(set(nums))
        nums.sort()
        #           [2, 3, 4, 5, 10]
        # i       = 2
        # currSeq = 4
        currSeq = 1
        maxSeq = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                currSeq += 1
                maxSeq = max(maxSeq, currSeq)
            else:
                currSeq = 1
        return maxSeq


test_cases = [
    [2, 20, 4, 10, 3, 4, 5],  # 4
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
]
s = Solution()
for t in test_cases:
    print(s.longestConsecutive(t))
