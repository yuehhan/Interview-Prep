class Solution:
    def isValid(self, s: str) -> bool:
        if s == "": return True
        stack = []
        for i in s:
            if stack and self.isCompliment(stack[-1],i):
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0
    
    def isCompliment(self, j, k):
        if j == '[' and k == ']':
            return True
        if j == '{' and k == '}':
            return True
        if j == '(' and k == ')':
            return True
        return False
        
