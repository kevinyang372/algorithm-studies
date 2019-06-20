# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3
 

# Note:
# Bonus points if you could solve it both recursively and iteratively

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    
    if not root: return True
    if not root.right and not root.left: return True
    if (root.right is None) ^ (root.left is None) : return False

    if root.right.val != root.left.val: 
        return False
    else:
        return check_symm(root.right, root.left)


def check_symm(node1, node2):

    if node1.val != node2.val:
        return False
    elif (node1.right is None) ^ (node2.left is None) or (node1.left is None) ^ (node2.right is None):
        return False

    check = True

    if node1.right and node2.left:
        check &= check_symm(node1.right, node2.left)
    
    if node1.left and node2.right:
        check &= check_symm(node1.left, node2.right)

    return check




