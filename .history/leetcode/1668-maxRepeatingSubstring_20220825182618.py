class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max = 0
        for k in range(1, len(sequence) // len(word) + 1):
            wordK = word * k
            if wordK in sequence:
                max = k
            else:
                return max
        return max


testCases = [("ababc", "ab"), ("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")]
s = Solution()
for t in testCases:
    print(s.maxRepeating(t[0], t[1]))
