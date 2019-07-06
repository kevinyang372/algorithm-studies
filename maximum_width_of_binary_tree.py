# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


# Note: Answer will in the range of 32-bit signed integer.

import collections

def widthOfBinaryTree(root):
    
    if not root: return 0
    
    stack = [[root, 0, 0]]
    max_width = 1
    d = collections.defaultdict(int)
    
    while stack:
        
        node, level, width = stack.pop(0)
        
        if d[level] == 0:
            d[level] = width
        elif width * d[level] > 0:
            max_width = max(max_width, width - d[level] + 1)
        else:
            max_width = max(max_width, width - d[level])
        
        if node.left:
            if width > 0:
                cur_width = width * 2 - 1
            elif width < 0:
                cur_width = width * 2
            else:
                cur_width = -1
            stack.append([node.left, level + 1, cur_width])
        
        if node.right:
            if width > 0:
                cur_width = width * 2
            elif width < 0:
                cur_width = width * 2 + 1
            else:
                cur_width = 1
            stack.append([node.right, level + 1, cur_width])
        
    return max_width