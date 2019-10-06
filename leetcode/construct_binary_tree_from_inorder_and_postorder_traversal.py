# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        
        if not inorder: return
        
        root = TreeNode(postorder[-1])
        ind = inorder.index(postorder[-1])
        length = len(inorder[:ind])
        
        root.left = buildTree(inorder[:ind], postorder[:length])
        root.right = buildTree(inorder[ind + 1:], postorder[length:-1])
        
        return root
        

# O(N) time optimization
def buildTree(inorder, postorder):

    if not inorder: return

    map_inorder = {}
    for k, v in enumerate(inorder): map_inorder[v] = k

    def helper(low, high):
        if low > high: return
        x = TreeNode(postorder.pop())
        mid = map_inorder[x.val]
        x.right = helper(mid + 1, high)
        x.left = helper(low, mid - 1)

        return x

    return helper(0, len(inorder) - 1)