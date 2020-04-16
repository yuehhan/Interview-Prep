def isSymmetric(self, root: TreeNode) -> bool:
    if not root: return True
    
    def symmetry(left, right):
        if not left and not right:
            return True
        if left and right:
            return left.val == right.val and symmetry(left.left, right.right) and                               symmetry(left.right, right.left)
        else:
            return False
    
    return symmetry(root.left, root.right)
    