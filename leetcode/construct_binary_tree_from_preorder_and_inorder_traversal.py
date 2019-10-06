# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):

    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])

    loc = inorder.index(preorder[0])
    left = loc + 1

    if loc > 0:
        for i in range(1, len(preorder[1:])):
            if preorder[i] not in inorder[:loc]:
                left = i
                break
        root.left = buildTree(preorder[1:left], inorder[:loc])

    if loc < len(inorder) - 1:
        root.right = buildTree(preorder[left:], inorder[loc + 1:])

    return root


# simple recursion
def buildTree(self, preorder, inorder):
    
    if not preorder: return
    root = TreeNode(preorder[0])
    ind = inorder.index(preorder[0])
    length = len(inorder[:ind])
    
    root.left = self.buildTree(preorder[1:1+length], inorder[:ind])
    root.right = self.buildTree(preorder[1+length:], inorder[ind + 1:])
    
    return root

# optimization
def buildTree(self, preorder, inorder):
    
    if not preorder: return
    map_inorder = {}
    for i,v in enumerate(inorder): map_inorder[v] = i

    def helper(low, high):
        if low > high: return
        x = TreeNode(preorder.pop(0))
        mid = map_inorder[x.val]
        x.left = helper(low, mid - 1)
        x.right = helper(mid + 1, high)
        return x

    return helper(0, len(inorder) - 1)