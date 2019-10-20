# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# recursive
def preorderTraversal(self, root):
    if not root: return []
    
    temp = [root.val]
    if root.left:
        temp += self.preorderTraversal(root.left)
    if root.right:
        temp += self.preorderTraversal(root.right)
        
    return temp

# iterative
def preorderTraversal(self, root):
        
    if not root: return []
    
    res = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return res