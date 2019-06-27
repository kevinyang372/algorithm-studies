# T l and T2 are two very large binary trees, with T l much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of Tl.
# A tree T2 is a subtree ofT i if there exists a node n in T i such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

cache = {}

def check_subtree(root1, root2):

    if not root1 or not root2: return False
    if not root1 and not root2: return True

    if root1.val == root2.val:
        if check_full(root1.left, root2.left):
            return True

    return check_subtree(root1.right, root2) or check_subtree(root1.left, root2)


def check_full(root1, root2):

    if not root1 and not root2: return True
    if not root1 or not root2: return False
    if (root1, root2) in cache: return cache[(root1, root2)]

    if root1.val == root2.val:
        res = check_full(root1.left, root2.left) and check_full(root1.right, root2.right)
    else:
        res = False

    cache[(root1, root2)] = res
    return res


# Could also be done by building the pre-order traversal of the two trees
# And compare if T1 contains T2 as substring