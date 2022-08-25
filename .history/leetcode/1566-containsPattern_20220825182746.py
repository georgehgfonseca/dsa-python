from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i = 0
        while i + m < len(arr):  # analysing patterns from i
            j = i
            curr = 1
            while j + m < len(arr):
                if j + m + 1 + m < len(arr) and arr[j : j + m] == arr[j + m + 1 : j + m + 1 + m]:
                    curr += 1
                    j += m
                    if curr >= k:
                        return True
                else:
                    break
            i += 1
        return False


testCases = [([1, 2, 1, 2, 1, 1, 1, 3], 2, 2)([1, 2, 4, 4, 4, 4], 1, 3)]
s = Solution()
for t in testCases:
    print(s.containsPattern(t[0], t[1], t[2]))
