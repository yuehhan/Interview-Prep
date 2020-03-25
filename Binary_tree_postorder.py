<<<<<<< HEAD
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

=======
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

>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return res[::-1]