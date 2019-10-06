# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

def rightSideView(self, root):
    if not root: return
    
    def helper(node):
        
        temp = [node.val]
        ri = []
        
        if node.right:
            ri = helper(node.right)
            temp += ri
        
        if node.left:
            temp += helper(node.left)[len(ri):]
            
        return temp
    
    return helper(root)