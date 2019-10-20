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

def widthOfBinaryTree(self, root):
    if not root: return 0
    
    queue = collections.deque([(root, 0, 0)])
    max_val = {}
    min_val = {}
    max_d = 0
    
    while queue:
        node, level, coordinate = queue.popleft()
        
        if level in max_val:
            max_val[level] = max(max_val[level], coordinate)
        else:
            max_val[level] = coordinate
            
        if level in min_val:
            min_val[level] = min(min_val[level], coordinate)
        else:
            min_val[level] = coordinate
            
        if max_val[level] * min_val[level] >= 0:
            max_d = max(max_d, max_val[level] - min_val[level] + 1)
        else:
            max_d = max(max_d, max_val[level] - min_val[level])
        
        if node.left:
            if coordinate == 0:
                res = -1
            elif coordinate > 0:
                res = coordinate * 2 - 1
            else:
                res = coordinate * 2
                
            queue.append((node.left, level + 1, res))
            
        if node.right:
            if coordinate == 0:
                res = 1
            elif coordinate > 0:
                res = coordinate * 2
            else:
                res = coordinate * 2 + 1
                
            queue.append((node.right, level + 1, res))
    
    return max_d