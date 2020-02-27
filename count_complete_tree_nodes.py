# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [root]
        res = []
        
        while root and stack:
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
            res.append(stack)
        
        return len(res)
                