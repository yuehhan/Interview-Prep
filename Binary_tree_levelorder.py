<<<<<<< HEAD
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        res = []
        
        while root and q:
            current = []
            nextlevel = []
            
            for node in q:
                current.append(node.val)
                
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
                
            res.append(current)
            q = nextlevel
        
        return res
=======
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        res = []
        
        while root and q:
            current = []
            nextlevel = []
            
            for node in q:
                current.append(node.val)
                
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
                
            res.append(current)
            q = nextlevel
        
        return res
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
