# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumOfLeftLeaves(root):

    if root.left is None and root.right is None:
        return 0

    sum_leaves = 0

    if root.left:
        if root.left.left is None and root.left.right is None:
            sum_leaves += (sumOfLeftLeaves(root.left) + root.left.val)
        else:
            sum_leaves += sumOfLeftLeaves(root.left)

    if root.right:
        sum_leaves += sumOfLeftLeaves(root.right)

    return sum_leaves