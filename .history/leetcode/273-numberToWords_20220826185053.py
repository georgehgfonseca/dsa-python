class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
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
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        numWord3 = {0: "", 1: " Thousand", 2: " Million", 3: " Billion", 4: " Trillion"}

        numArr = numArr[::-1]  # reversed array is easier to handle
        for i in range(0, (len(numArr) // 3) + 1):  # process 3-digit block each time
            idx1 = i * 3
            idx2 = i * 3 + 1
            idx3 = i * 3 + 2
            hasIdx1 = True if idx1 < len(numArr) else False
            hasIdx2 = True if idx2 < len(numArr) else False
            hasIdx3 = True if idx3 < len(numArr) else False
            if not hasIdx1:
                return ans.strip()
            if hasIdx1 and idx1 == 0 and hasIdx2 and idx2 == 0 and hasIdx3 and idx3 == 0:
                continue
            threeDigitStr = ""
            if hasIdx3:
                if numArr[idx3] != 0:
                    threeDigitStr = numWord1[numArr[idx3]] + " Hundred" + threeDigitStr
                    if numArr[idx2] == 1:
                        threeDigitStr = threeDigitStr + " " + numWord1b[numArr[idx1]]
                    elif numArr[idx2] != 0:
                        threeDigitStr = threeDigitStr + " " + numWord2[numArr[idx2]] + " " + numWord1[numArr[idx1]]
                    else:
                        threeDigitStr = threeDigitStr + " " + numWord1[numArr[idx1]]
                else:
                    if numArr[idx2] == 1:
                        threeDigitStr = numWord1b[numArr[idx1]] + " " + threeDigitStr
                    elif numArr[idx2] != 0:
                        threeDigitStr = numWord2[numArr[idx2]] + " " + numWord1[numArr[idx1]] + " " + threeDigitStr
                    else:
                        threeDigitStr = numWord1[numArr[idx1]] + " " + threeDigitStr
            elif hasIdx2:
                if numArr[idx2] == 1:
                    threeDigitStr = numWord1b[numArr[idx1]] + " " + threeDigitStr
                elif numArr[idx2] != 0:
                    threeDigitStr = numWord2[numArr[idx2]] + " " + numWord1[numArr[idx1]] + " " + threeDigitStr
                else:
                    threeDigitStr = numWord1[numArr[idx1]] + " " + threeDigitStr
            elif hasIdx1:
                threeDigitStr = numWord1[numArr[idx1]] + " " + threeDigitStr
            ans = threeDigitStr.strip() + numWord3[i] + " " + ans
        return ans.strip()


testCases = [1000000, 110, 123, 1234567, 12345, 10, 3, 5, 49]
s = Solution()
for t in testCases:
    print(s.numberToWords(t))
