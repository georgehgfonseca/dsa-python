class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        numArr = []
        while num > 0:
            numArr = [num % 10] + numArr
            num = num // 10

        numWord1 = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        numWord1b = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen",
        }
        numWord2 = {
            0: "",
            1: "",
            2: "Twenty",
            3: "Thirty",
            4: "Fourty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        numWord3 = {0: "", 1: "Hundred", 2: "Thousand", 3: "Million", 4: "Billion", 5: "Trillion"}

        numArr = numArr[-1:] # reversed array is easier to handle
        for i in range(0, len(numArr) // 3): # process 3-digit block each time 
            if i * 3 < len(numArr) and i * 3 + 1 < len(numArr) and i * 3 + 2 < len(numArr): # process 3rd digit
                ans = numArr[i * 3 + 2] + numWord3[i] + ans
            for j in range(i * 3, i * 3 + 3):
                if :
                    ans = numWord1 + ans
                
                ans = ans

        return ans


testCases = [10, 3, 5, 49]
s = Solution()
for t in testCases:
    print(s.intToRoman(t))
