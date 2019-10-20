# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

# You may assume each number in the sequence is unique.

# Consider the following binary search tree: 

#      5
#     / \
#    2   6
#   / \
#  1   3
# Example 1:

# Input: [5,2,6,1,3]
# Output: false
# Example 2:

# Input: [5,2,1,3,6]
# Output: true
# Follow up:
# Could you do it using only constant space complexity?

# recursive approach
def verifyPreorder(self, preorder):
        
    def traverse(ind, lower, upper):
        if ind == len(preorder): return True
        
        node = preorder[ind]
        
        if node < lower: 
            return False
        
        if ind == len(preorder) - 1:
            return True
        elif preorder[ind + 1] < node:
            res = traverse(ind + 1, lower, node)
            if res == True:
                return True
            elif res == False:
                return False
            elif preorder[res] > upper:
                return res
            else:
                return traverse(res, node, upper)
        elif preorder[ind + 1] > upper:
            return ind + 1
        else:
            return traverse(ind + 1, node, upper)
            
            
    return traverse(0, -float('inf'), float('inf'))

# stack approach
def verifyPreorder(self, preorder):
        
    if not preorder: return True
    
    stack = [preorder[0]]
    prev_root = None
    
    for ind in range(1, len(preorder)):
        if prev_root and preorder[ind] < prev_root:
            return False
        
        while stack and preorder[ind] > stack[-1]:
            prev_root = stack.pop()
        
        stack.append(preorder[ind])
    
    return True