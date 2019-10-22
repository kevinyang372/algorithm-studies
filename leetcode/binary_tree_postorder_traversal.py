# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?

def postorderTraversal(self, root):
    if not root: return
    temp = []
    if root.left:
        temp += self.postorderTraversal(root.left)
    if root.right:
        temp += self.postorderTraversal(root.right)
    
    temp.append(root.val)
    return temp

# iterative
def postorderTraversal(self, root):
    if not root: return 
    stack = [root]
    res = []
    
    while stack:
        node = stack.pop()
        
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        
    return res[::-1]