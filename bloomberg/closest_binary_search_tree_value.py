# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:

# Input: root = [4,2,5,1,3], target = 3.714286

#     4
#    / \
#   2   5
#  / \
# 1   3

# Output: 4

# O(N) solution
def closestValue(self, root, target):
        
    def traverse(node):
        if not node: return float('inf')
        return min(node.val, traverse(node.left), traverse(node.right), key=lambda x:abs(x - target))
        
    return traverse(root)

# O(logN) solution (Binary search)
def closestValue(self, root, target):
    min_val = root.val
    
    while root:
        min_val = min(root.val, min_val, key=lambda x: abs(target - x))
        if target > root.val:
            root = root.right
        else:
            root = root.left
    
    return min_val