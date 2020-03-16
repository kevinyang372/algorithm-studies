# Given a binary search tree, return a balanced binary search tree with the same node values.

# A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

# If there is more than one answer, return any of them.

 

# Example 1:



# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The tree nodes will have distinct values between 1 and 10^5.

def balanceBST(self, root: TreeNode) -> TreeNode:
        
    def decompose(node):
        if not node: return []
        left, right = node.left, node.right
        node.left = None
        node.right = None
        return decompose(left) + [node] + decompose(right)
    
    def construct(a):
        if len(a) == 1: return a[0]
        if not a: return None
        
        curr = a[len(a) // 2]
        curr.left = construct(a[:len(a) // 2])
        curr.right = construct(a[len(a) // 2 + 1:])
        
        return curr
    
    return construct(decompose(root))