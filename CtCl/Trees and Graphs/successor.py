# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def successor(node):

    if not node: return

    if node.right: 
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp
    else:
        temp = node.parent
        while temp and temp.left != temp:
            node, temp = temp, temp.parent
        return temp