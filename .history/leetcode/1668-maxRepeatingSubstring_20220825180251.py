class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        lenWord = len(word)
        for i in range(len(sequence)):
            if sequence[i : i + lenWord] == word:
                ans += 1
        return ans


testCases = [("ababc", "ab")]
s = Solution()
for t in testCases:
    print(s.maxRepeating(t[0], t[1]))
