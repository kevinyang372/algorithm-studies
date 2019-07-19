# Given a tree. Root is level 0. Level is defined as left child is root level - 1, right child is root level + 1. Return a map of level number and its sum.

#      3
#     / \
#    2   4
#   / \
# -1   7
# Ans should be {-2:-1, -1:2, 0:10, 1:4}
# 7 is level 0 because it is left then right child of root, so its level is 0-1+1 == 0

def verticalLevelsum(root):
    
    d = collections.defaultdict(int)

    def helper(node, x):
        if not node: return

        d[x] += node.val
        helper(node.left, x - 1)
        helper(node.right, x + 1)

    helper(root, 0)
    return d