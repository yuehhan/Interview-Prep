class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        
        stack = []
        self.helper(root, stack)
        return root
    
    def helper(self,root,stack):
    
        if root.right:
            stack.append(root.right)
        
        if root.left:
            self.helper(root.left, stack)
            root.right = root.left
            root.left = None
            
            
        if not root.left and stack:
            node = stack.pop()
            root.right = node
        
        
            
