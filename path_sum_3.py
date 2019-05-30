# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root, num_sum):

    if not root:
        return 0
    
    stack = [[root, root.val]]
    num = 1 if root.val == num_sum else 0
    checked_nodes = [root]

    while stack:

        re = stack.pop()

        if re[0].right:
            right = re[1] + re[0].right.val

            if right == num_sum:
                num += 1
            if re[0].right not in checked_nodes:
                if re[0].right.val == num_sum:
                    num += 1
                checked_nodes.append(re[0].right)
                stack.append([re[0].right, re[0].right.val])

            stack.append([re[0].right, right])

        if re[0].left:
            left = re[1] + re[0].left.val

            if left == num_sum:
                num += 1
            if re[0].left not in checked_nodes:
                if re[0].left.val == num_sum:
                    num += 1
                checked_nodes.append(re[0].left)
                stack.append([re[0].left, re[0].left.val])

            stack.append([re[0].left, left])

    return num
