from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        i = 0
        while i < len(arr):  # analysing patterns from i
            j = i
            curr = 1
            while j + m < len(arr):
                print(arr[j : j + m], arr[j + m : j + m + m])
                if j + m + m <= len(arr) and arr[j : j + m] == arr[j + m : j + m + m]:
                    curr += 1
                    j += m
                    if curr >= k:
                        return True
                else:
                    break
            i += 1
        return False


testCases = [(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")]
s = Solution()
for t in testCases:
    print(s.isAlienSorted(t[0], t[1]))
