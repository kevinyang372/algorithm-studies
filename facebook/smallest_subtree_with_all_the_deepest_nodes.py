# Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

# A node is deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is that node, plus the set of all descendants of that node.

# Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

# Example 1:

# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def subtreeWithAllDeepest(root):

    if not root: return None

    deepest = ['0']
    stack = [[root, '0']]

    while stack:
        node, code = stack.pop(0)

        if len(code) == len(deepest[0]):
            deepest.append(code)
        elif len(code) > len(deepest[0]):
            deepest = [code]

        if node.left:
            code_l = code + '0'
            stack.append([node.left, code_l])

        if node.right:
            code_r = code + '1'
            stack.append([node.right, code_r])

    for i in range(1, len(deepest[0])):
        d = deepest[0][i]
        for m in deepest:
            if m[i] != d:
                return root
            
        if d == '1':
            root = root.right
        else:
            root = root.left
    
    return root