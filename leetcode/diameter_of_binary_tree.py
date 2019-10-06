# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursive
def diameterOfBinaryTree(root):

    if not root: return 0

    return max(search(root.right, 0) + search(root.left, 0), diameterOfBinaryTree(root.right), diameterOfBinaryTree(root.left))

def search(root, curr):

    if not root: return curr

    return max(search(root.left, curr + 1), search(root.right, curr + 1))



# caching
cache = {}

def diameterOfBinaryTree(root):

    if not root: return 0

    return max(search(root.right, 0) + search(root.left, 0), diameterOfBinaryTree(root.right), diameterOfBinaryTree(root.left))

def search(root, curr):

    if not root: return curr
    if head in cache: return cache[head] + curr + 1

    val = max(search(head.left, 0), search(head.right, 0))
    cache[head] = val
    return val + curr + 1