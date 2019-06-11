# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def countNodes(root):

    stack = [root]
    counter = 0

    while stack:

        node = stack.pop(0)
        counter += 1

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return counter
        