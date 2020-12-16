# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root: TreeNode, min_val = None, max_val = None) -> bool:

    if not root:
        return True

    if root.right:
        if root.right.val <= root.val:
            return False
        elif max_val and root.right.val >= max_val:
            return False
        elif not isValidBST(root.right, min_val = root.val, max_val = max_val):
            return False

    if root.left:
        if root.left.val >= root.val:
            return False
        elif min_val and root.left.val <= min_val:
            return False
        elif not isValidBST(root.left, min_val = min_val, max_val = root.val):
            return False

    return True


# more concise version
def isValidBST(self, root: TreeNode) -> bool:
    def validate(node, maximum, minimum):
        if not node:
            return True
        if node.val >= maximum or node.val <= minimum:
            return False
        return validate(node.left, node.val, minimum) and validate(node.right, maximum, node.val)
    return validate(root, float('inf'), -float('inf'))
