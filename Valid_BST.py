# Using Inorder Traversal
def isValidBST(self, root: TreeNode) -> bool:
        output = []
        self.inOrder(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

def inOrder(self, root, output):
    if root is None:
        return

    self.inOrder(root.left, output)
    output.append(root.val)
    self.inOrder(root.right, output)