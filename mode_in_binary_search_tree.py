# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findMode(root):

    if root.left is None and root.right is None:
        return {root.val: 1}

    dic_left = {}
    dic_right = {}

    if root.left is not None:
        dic_left = findMode(root.left)

    if root.right is not None:
        dic_right = findMode(root.right)

    for i in dic_right.keys():
        if i in dic_left.keys():
            dic_left[i] += dic_right[i]
        else:
            dic_left[i] = dic_right[i]

    if root.val in dic_left:
        dic_left[root.val] += 1
    else:
        dic_left[root.val] = 1

    return dic_left