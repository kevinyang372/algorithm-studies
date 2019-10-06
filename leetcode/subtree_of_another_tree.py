# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

def isSubtree(self, s, t):
        
    def check(node1, node2):
        if not node1 and not node2: return True
        if (not node1 and node2) or (node1 and not node2): return False
        
        res = False
        if node1.val == node2.val:
            res = check_all(node1.left, node2.left) and check_all(node1.right, node2.right)
            
        update = check(node1.left, node2) or check(node1.right, node2)
        return res or update
    
    def check_all(node1, node2):
        if not node1 and not node2: return True
        if (not node1 and node2) or (node1 and not node2): return False
        
        return node1.val == node2.val and check_all(node1.left, node2.left) and check_all(node1.right, node2.right)
    
    return check(s, t)