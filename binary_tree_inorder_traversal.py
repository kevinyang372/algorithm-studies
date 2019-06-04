# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root: TreeNode):

    if not root:
        return []

    curr = root.val
    le = inorderTraversal(root.left)
    ri = inorderTraversal(root.right)

    return le + [curr] + ri

def inorderTraversal(root:TreeNode):

    res, stack = [], []

    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack: return res
        node = stack.pop()
        res.append(node.val)
        root = node.right

