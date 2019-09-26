# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

# Example 1:



# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
 

# Constraints:

# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def delNodes(self, root, to_delete):
    if not to_delete: return [root]
    if not root: return []
    
    delete = []
    
    def explore_tree(node):
        if not node: return True
        if node.val in to_delete:
            if node.left:
                delete.append(node.left)
            if node.right:
                delete.append(node.right)
            return False
        else:
            if not explore_tree(node.left):
                node.left = None
            if not explore_tree(node.right):
                node.right = None
            return True
    
     
    if root.val in to_delete:
        return self.delNodes(root.left, to_delete) + self.delNodes(root.right, to_delete)
    else:
        explore_tree(root)
        res = [root]
        for i in delete:
            res += self.delNodes(i, to_delete)
            
        return res