from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_chars = {
            "2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"},
        }

        combinations = []
        def helper(index, curr_comb):
            if index > len(digits) - 1:
                combinations.append(curr_comb)
                return

            for char in digit_chars[digits[index]]:
                curr_comb_temp = curr_comb[:] + char
                helper(index + 1, curr_comb_temp)

        if not digits:
            return []
            
        helper(0, "")
        return combinations
        

testCases = [
    "23"
]

s = Solution()
for t in testCases:
    print(s.letterCombinations(t))