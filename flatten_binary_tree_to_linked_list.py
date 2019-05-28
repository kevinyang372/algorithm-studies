# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def flatten(root):

  stack = []
  current_node = root

  while current_node:

    if current_node.right:
      stack.append(current_node.right)

    if current_node.left:
      stack.append(current_node.left)

    if len(stack) == 0:
      break

    temp = stack.pop()
    current_node.right = temp
    current_node.left = None

    current_node = temp

