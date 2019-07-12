# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root: TreeNode):

    if not root:
        return []

    curr = root.val
    le = inorderTraversal(root.left)
    ri = inorderTraversal(root.right)

    return le + [curr] + ri

# inorder traversal iterative
def inorderTraversal(self, root):
    if not root: return []
    
    stack = [root]
    res = []
    visited = set()
    
    while stack:
        node = stack[-1]
        
        if node.left and node.left not in visited:
            stack.append(node.left)
        else:
            res.append(node.val)
            stack.pop()
            visited.add(node)
            if node.right:
                stack.append(node.right)
                
    return res

