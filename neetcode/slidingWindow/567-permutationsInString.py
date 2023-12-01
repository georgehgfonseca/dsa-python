from typing import List

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_count = {}
        for char in s1:
            if char not in s1_char_count:
                s1_char_count[char] = 1
            else:
                s1_char_count[char] += 1
        
        start = 0
        end = 0
        s2_window_char_count = {}
        while end < len(s2):
            curr_char = s2[end]
            if curr_char not in s2_window_char_count:
                s2_window_char_count[curr_char] = 1
            else:
                s2_window_char_count[curr_char] += 1
            
            # check if char counts of s1 and s2_window are equal
            if len(s1_char_count) <= len(s2_window_char_count):
                are_equal = True
                for char in s1_char_count:
                    if char not in s2_window_char_count or s1_char_count[char] != s2_window_char_count[char]:
                        are_equal = False
                        break
                if are_equal:
                    return True
            
            if (end + 1 - start) == len(s1):
                s2_window_char_count[s2[start]] -= 1
                start += 1
            
            end += 1
        return False


testCases = [
    ("ab", "eidbaooo"),    # True
    ("ab", "eidboaoo"),    # False
]

s = Solution()
for t in testCases:
    print(s.checkInclusion(t[0], t[1]))