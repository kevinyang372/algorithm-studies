# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

# Example 1:

# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# Example 2:

# Input: "1,#"
# Output: false
# Example 3:

# Input: "9,#,#,1"
# Output: false

def isValidSerialization(self, preorder):
        
    if preorder[0] == "#": 
        if len(preorder) == 1: 
            return True
        else:
            return False
    
    preorder = preorder.split(',')
    stack = [[None, None]]
    count = 1
    
    for i in preorder[1:]:
        if not stack: return False
        if i == '#':
            if not stack[-1][0]:
                stack[-1][0] = True
            else:
                stack[-1][1] = True
        else:
            if not stack[-1][0]:
                stack[-1][0] = count
            else:
                stack[-1][1] = count
            stack.append([None, None])
            count += 1
        
        while stack and all(stack[-1]):
            stack.pop()
    
    return len(stack) == 0