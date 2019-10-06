# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

def binaryTreePaths(self, root):
    if not root: return
    
    def path(node):
        if not node.left and not node.right: return [str(node.val)]
        
        res = []
        if node.right:
            res += ['%s->%s' % (node.val, i) for i in path(node.right)]
        if node.left:
            res += ['%s->%s' % (node.val, i) for i in path(node.left)]
            
        return res
    
    return path(root)