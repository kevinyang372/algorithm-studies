# Given a binary tree, we install cameras on the nodes of the tree. 

# Each camera at a node can monitor its parent, itself, and its immediate children.

# Calculate the minimum number of cameras needed to monitor all nodes of the tree.

# https://leetcode.com/problems/binary-tree-cameras/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minCameraCover(root):

    re = []
    covered = set()
    stack = [root]

    while stack:

        node = stack.pop()

        if isleaf(node):
            covered.add(node)
        
        re = [node] + re

        if node.left:
            if node.left.left or node.left.right:
                stack.append(node.left)

        if node.right:
            if node.right.left or node.right.right:
                stack.append(node.right)

    need_to_be_covered = set()
                
    for i in re:
        if i in covered:
            need_to_be_covered.discard(i.left)
            need_to_be_covered.discard(i.right)
            continue
        
        if i.left in need_to_be_covered or i.right in need_to_be_covered:
            covered.add(i)
            need_to_be_covered.discard(i.left)
            need_to_be_covered.discard(i.right)
            continue
        
        if i.left in covered or i.right in covered:
            continue
        
        need_to_be_covered.add(i)

    return len(covered) + len(need_to_be_covered)

def isleaf(root):

    if root.left:
        if not root.left.left and not root.left.right:
            return True

    if root.right:
        if not root.right.left and not root.right.right:
            return True

    return False

