# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                res.append(node.val)                
                stack.append(node.left)
                stack.append(node.right)

        return res[::-1]