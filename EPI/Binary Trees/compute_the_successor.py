# The successor of a node in a binary tree is the node that appears immediately after the given node in an inorder traversal. Design an algorithm that computes the successor of a node in a binary tree. Assume that each node stores its parent.

def findSuccessor(node):

    if node.right:
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp

    if node.parent:
        while node.parent and node.parent.right != node:
            node = node.parent
        return node if node.parent else None

    return None