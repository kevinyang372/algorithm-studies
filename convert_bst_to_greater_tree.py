# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# Example:

# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13

# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convertBST(root):

    _sum = 0

    def dfs(root):
        if not root:
            return
        
        dfs(root.right)
        
        root.val += _sum
        
        _sum = root.val
        
        dfs(root.left)
        
    dfs(root)
    return root







