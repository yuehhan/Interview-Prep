class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for i in S:
            if stack == [] or stack[-1] != i:
                stack.append(i)
            else:
                stack.pop()
        return ''.join(stack)
            