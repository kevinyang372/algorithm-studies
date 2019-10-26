# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# Example :

# Input:  root = [5,1,5,5,5,null,5]

#               5
#              / \
#             1   5
#            / \   \
#           5   5   5

# Output: 4

def countUnivalSubtrees(self, root):
        
    if not root: return 0
    
    def search(node):
        left = right = cur = str(node.val)
        count = 0
        
        if node.right:
            right, temp = search(node.right)
            count += temp
            
        if node.left:
            left, temp = search(node.left)
            count += temp
        
        if cur == right == left:
            return cur, count + 1
        else:
            return False, count
        
    return search(root)[1]