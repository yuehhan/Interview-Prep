<<<<<<< HEAD
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:   
        res = []
        stack = [root]
        
        while stack and root:
            node = stack.pop()
            
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
=======
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:   
        res = []
        stack = [root]
        
        while stack and root:
            node = stack.pop()
            
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
        return res