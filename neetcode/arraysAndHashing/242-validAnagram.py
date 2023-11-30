class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
         
        letter_occurencies_s = {}
        for letter in s:
            if letter not in letter_occurencies_s:
                letter_occurencies_s[letter] = 1
            else:
                letter_occurencies_s[letter] += 1
        
        letter_occurencies_t = {}
        for letter in t:
            if letter not in letter_occurencies_t:
                letter_occurencies_t[letter] = 1
            else:
                letter_occurencies_t[letter] += 1
        
        for letter in letter_occurencies_t:
            if letter not in letter_occurencies_s:
                return False
            if letter_occurencies_t[letter] != letter_occurencies_s[letter]:
                return False
        
        return True
               


test_cases = [
    ("anagram", "nagaram"), # True
    ("rat", "car")          # False
]
s = Solution()
for t in test_cases:
    print(s.isAnagram(t[0], t[1]))