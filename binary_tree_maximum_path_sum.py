# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root):

    if root.left is None and root.right is None:
        return root.val

    max_result = root.val
    left = maxPathSearch(root.left) 
    right = maxPathSearch(root.right)
    
    if left > 0:
        max_result = max_result + left
    
    if right > 0:
        max_result = max_result + right

    if root.left:
        max_result = max(maxPathSum(root.left), max_result)

    if root.right:
        max_result = max(maxPathSum(root.right), max_result)

    return max_result


def maxPathSearch(root):

    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.val

    max_result = root.val
    
    if root.left:
        max_result = max(max_result, root.val + maxPathSearch(root.left))

    if root.right:
        max_result = max(max_result, root.val + maxPathSearch(root.right))

    return max_result
