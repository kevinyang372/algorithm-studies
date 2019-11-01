# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# The length of path between two nodes is represented by the number of edges between them.

 

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2

 

# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2

 

# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

def longestUnivaluePath(self, root):
        
    if not root: return 0
    
    def traverse(node):
        l = r = l1 = r1 = sums = 0
        if node.left:
            l, l1 = traverse(node.left)
            if node.left.val == node.val:
                l += 1
            else:
                l = 0
                
        if node.right:
            r, r1 = traverse(node.right)
            if node.right.val == node.val:
                r += 1
            else:
                r = 0
        
        if node.left and node.left.val == node.val:
            sums += l
        if node.right and node.right.val == node.val:
            if sums != 0:
                sums += r - 1
            else:
                sums += r
            
        return max(l, r, 1),  max(l1, r1, sums)
    
    return max(0, traverse(root)[1] - 1)