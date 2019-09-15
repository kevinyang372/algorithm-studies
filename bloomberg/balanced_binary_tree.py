# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

def isBalanced(self, root):
    if not root: return True
    def check(node):
        left = right = 0
        if node.left:
            left = check(node.left) + 1
        if node.right:
            right = check(node.right) + 1
            
        if abs(left - right) > 1 or left < 0 or right < 0:
            return -float('inf')
            
        return max(left, right)
    
    return check(root) >= 0