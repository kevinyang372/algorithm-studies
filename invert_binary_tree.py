# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

def invertTree(root):

    if root:
        root.left, root.right = root.right, root.left
        invertTree(root.left)
        invertTree(root.right)

    return root