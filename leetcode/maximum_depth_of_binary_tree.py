# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):

    max_d = 0
    stack = [[root, 0]]

    while stack:

        node, level = stack.pop(0)

        if node.right:
            max_d = max(max_d, level + 1)
            stack.append([node.right, level + 1])

        if node.left:
            max_d = max(max_d, level + 1)
            stack.append([node.left, level + 1])

    return max_d
