class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        inSubtr = {}
        i = 0
        while i < len(s):
            if s[i] not in inSubtr:
                inSubtr[s[i]] = i
                max += 1
            else:
                # return i to last valid state
                i = inSubtr[s[i]]
                # reset everything
                inSubtr = {}
                max = 0
            i += 1
        return max


testCases = ["abcabcbb", "bbbbb", "pwwkew"]
s = Solution()
for t in testCases:
    print(s.lengthOfLongestSubstring(t))
