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

def flatten(self, root):
    def helper(node):
        if not node: return
        if node.left:
            endpoint = helper(node.left)
        else:
            if node.right:
                res = helper(node.right)
                return res
            else:
                return node
        
        if node.right:
            e2 = helper(node.right)
        else:
            e2 = endpoint
        
        endpoint.right = node.right
        node.right = node.left
        node.left = None
        
        return e2
        
    helper(root)

