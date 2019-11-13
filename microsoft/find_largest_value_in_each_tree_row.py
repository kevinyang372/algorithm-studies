# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]

def largestValues(self, root):
        
    if not root: return
    
    stack = [root]
    res = []
    
    while stack:
        max_val = -float('inf')
        temp = []
        
        for i in stack:
            max_val = max(i.val, max_val)
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        
        stack = temp
        res.append(max_val)
    
    return res