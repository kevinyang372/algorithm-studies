# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:

# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 9

# Output: True
 

# Example 2:

# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 28

# Output: False

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Hash map
def findTarget(root, k):
    if not root: return False
    
    seen = set()
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        if k - node.val in seen:
            return True
        
        seen.add(node.val)
        
        if node.left:
            stack.append(node.left)
        
        if node.right:
            stack.append(node.right)
            
    return False