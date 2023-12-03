from typing import List
import math

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = list()
        res = 0
        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                if len(operand_stack) < 2:
                    # invalid entry
                    return -1
                # perform operation with 2 prev operands
                operand2 = operand_stack.pop() 
                operand1 = operand_stack.pop() 
                if tokens[i] == "+":
                    res = operand1 + operand2
                elif tokens[i] == "-":
                    res = operand1 - operand2
                elif tokens[i] == "*":
                    res = operand1 * operand2
                elif tokens[i] == "/":
                    res = operand1 / operand2
                    res = math.floor(res) if res > 0 else math.ceil(res)
                operand_stack.append(res)
            else:
                # push operand to the stack
                operand_stack.append(int(tokens[i]))
        return res
                 
        
    
testCases = [
    ["2","1","+","3","*"],   # 9 
    ["4","13","5","/","+"],  # 6
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],  # 22
] 

s = Solution()
for t in testCases:
    print(s.evalRPN(t))
