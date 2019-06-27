# A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
# EXAMPLE Input:
# Output: {2, 1, 3}, {2, 3, 1}

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bst(root):

    if not root: return 

    le = bst(root.left)
    ri = bst(root.right)

    res = [[root] + i for i in weave(le, ri)]

    return res


def weave(lis1, lis2, pre = []):
    
    if not lis1 and not lis2:
        return [pre]
    if not lis1 or not lis2:
        return [pre + lis1 + lis2]

    res = weave(lis1[1:], lis2, pre + [lis1[0]])
    res += weave(lis1, lis2[1:], pre + [lis2[0]])

    return res

