import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        checks=["+","-","/","*"]
        
        for i in range(len(tokens)):
            if tokens[i] not in checks:
                stack.append(int(tokens[i]))
            else:
                if stack:
                    b= stack.pop()
                    a=stack.pop()
                    if tokens[i] == "+":
                        stack.append(a + b)
                    elif tokens[i] == "-":
                        stack.append(a - b)
                    elif tokens[i] == "*":
                        stack.append(a * b)
                    elif tokens[i] == "/":
                        stack.append(int(a / b))
                    
        return stack[-1]