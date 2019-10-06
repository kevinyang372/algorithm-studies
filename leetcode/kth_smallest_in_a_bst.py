# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root, k):

    if not root: return

    stack = [root]
    seen = set()
    count = 0

    while stack:
        node = stack[-1]

        if node.left and node.left not in seen:
            stack.append(node.left)
        else:
            count += 1
            if count == k: return node.val

            stack.pop()
            seen.add(node)
            if node.right: stack.append(node.right)

    return 