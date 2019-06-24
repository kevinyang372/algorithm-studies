# Given a sorted (increasing order) array with unique integer elements, write an algo- rithm to create a binary search tree with minimal height.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def balanced_bst(lis):

    if len(lis) < 1 or lis[0] > lis[-1]: return

    mid = len(lis) // 2

    root = TreeNode(lis[mid])
    root.left = balanced_bst(lis[:mid])
    root.right = balanced_bst(lis[mid + 1:])

    return root