# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

def pathSum(self, root, sum):
    if not root: return []
    if root.val == sum and not root.left and not root.right: return [[root.val]]
    
    res = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
    return [[root.val] + i for i in res]