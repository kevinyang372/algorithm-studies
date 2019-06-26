# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def common_ancestor(root, node1, node2):

    if not cover(root, node1) or not cover(root, node2):
        return

    if cover(root.left, node1) and cover(root.left, node2):
        return common_ancestor(root.left, node1, node2)
    elif cover(root.right, node1) and cover(root.right, node2):
        return common_ancestor(root.right, node1, node2)
    else:
        return root


def cover(root, node1):

    if not root: return False
    if root == node1: return True

    return cover(root.left, node1) or cover(root.right, node2)