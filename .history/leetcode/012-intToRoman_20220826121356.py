class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        digitWeight = 1
        numRoman1 = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        numRoman2 = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        numRoman3 = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        while num > 0:
            curr = num % 10
            num = num // 10
            if digitWeight == 1:
                ans = numRoman1[curr] + ans
            elif digitWeight == 2:
                ans = numRoman2[curr] + ans
            elif digitWeight == 3:
                ans = numRoman3[curr] + ans
            elif digitWeight == 4:  # only up to 3999 is allowed
                ans = ("M" * curr) + ans
            digitWeight += 1
        return ans


testCases = [3, 5, 49]
s = Solution()
for t in testCases:
    print(s.intToRoman(t))
