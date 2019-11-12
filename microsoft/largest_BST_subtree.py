# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

# Note:
# A subtree must include all of its descendants.

# Example:

# Input: [10,5,15,1,8,null,7]

#    10 
#    / \ 
#   5  15 
#  / \   \ 
# 1   8   7

# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
#              The return value is the subtree's size, which is 3.
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?

def largestBSTSubtree(self, root):
        
    if not root: return 0
    
    def traverse(node, visited):
        
        if node.val in visited:
            seen = True
        else:
            seen = False
            
        visited.add(node.val)
        
        c1 = c2 = True
        sl = sr = msl = msr = 0
        min_l = min_r = node.val
        max_l = max_r = node.val
        
        if node.left:
            c1, sl, msl, min_l, max_l = traverse(node.left, visited)
        if node.right:
            c2, sr, msr, min_r, max_r = traverse(node.right, visited)
        
        if max_l > node.val or min_r < node.val or seen:
            flag = False
        else:
            flag = True
        
        if c1 and c2 and flag:
            return flag, sl + sr + 1, sl + sr + 1, min_l, max_r
        else:
            return False, sl + sr + 1, max(msl, msr), min(min_l, min_r), max(max_l, max_r)
        
    return traverse(root, set())[2]