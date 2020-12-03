# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:


# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
 

# Constraints:

# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000

def increasingBST(self, root: TreeNode) -> TreeNode:
        
    def expand(r):
        if not r: return None, None
        
        node = r
        stack = []

        while node.left:
            stack.append(node)
            
            temp = node.left
            node.left = None
            node = temp

        stack.append(node)
        head = tail = stack[-1]
        
        while stack:
            n = stack.pop()
            
            if tail != n:
                tail.right = n
                tail = n
                
            if n.right:
                temp_h, temp_t = expand(n.right)
                n.right, tail = temp_h, temp_t
        
        return head, tail
    
    return expand(root)[0]