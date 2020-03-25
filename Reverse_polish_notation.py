<<<<<<< HEAD
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sign = "+-*/"
        for i in tokens:
            if i in sign:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(a/b)
            else:
                stack.append(i)
                
        return int(stack.pop())
    
=======
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sign = "+-*/"
        for i in tokens:
            if i in sign:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(a/b)
            else:
                stack.append(i)
                
        return int(stack.pop())
    
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
    