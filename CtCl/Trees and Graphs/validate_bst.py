 # Implement a function to check if a binary tree is a binary search tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# use in-order traversal
def validate_bst(root):

    stack = []
    inorder = float('-inf')

    while stack and root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right

    return True
