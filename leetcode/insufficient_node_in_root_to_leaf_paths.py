# Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

# A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

# Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

 

# Example 1:


# Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

# Output: [1,2,3,4,null,null,7,8,9,null,14]
# Example 2:


# Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

# Output: [5,4,8,11,null,17,4,7,null,null,null,5]
 

# Example 3:


# Input: root = [1,2,-3,-5,null,4,null], limit = -1

# Output: [1,null,-3,4]

def sufficientSubset(root, limit):
    if not root: return
    
    def helper(node, prev_sum):
        
        if not node.left and not node.right:
            return node.val
        
        curr_sum = prev_sum + node.val
        le = ri = -float('inf')
        
        if node.left:
            le = helper(node.left, curr_sum)
            if curr_sum + le < limit:
                node.left = None
            
        if node.right:
            ri = helper(node.right, curr_sum)
            if curr_sum + ri < limit:
                node.right = None
            
        return node.val + max(le, ri)
    
    res = helper(root, 0)
    
    if res < limit:
        return 
    else:
        return root