class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in S:
            if stack == []:
                stack.append(i)
            elif stack[-1] == "(" and i == ")":
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack)