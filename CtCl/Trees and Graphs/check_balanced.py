# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def check_balanced(root):

    if not root: return True

    if abs(check_depth(root.left, 0) - check_depth(root.right, 0)) < 2:
        return check_balanced(root.left) and check_balanced(root.right)

    return False


def check_depth(root, cur):
    
    if not root: return cur

    return max(check_depth(root.left, cur + 1), check_depth(root.right, cur + 1))