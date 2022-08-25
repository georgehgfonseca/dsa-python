class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        lenWord = len(word)
        for i in range(len(str)):
            if str[i:lenWord] == word:
                ans += 1
        return ans


testCases = [("ababc", "ab")]
s = Solution()
for t in testCases:
    print(s.addTwoNumbers(t[0], t[1]))
