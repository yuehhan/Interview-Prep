<<<<<<< HEAD
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
        
=======
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
        
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return len(stack)