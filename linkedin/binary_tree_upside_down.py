# Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

# Example:

# Input: [1,2,3,4,5]

#     1
#    / \
#   2   3
#  / \
# 4   5

# Output: return the root of the binary tree [4,5,2,#,#,3,1]

#    4
#   / \
#  5   2
#     / \
#    3   1  
# Clarification:

# Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.

# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

# Here's an example:

#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].

def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        
    if not root: return
    
    def traverse(node, prev, prev_l):
        temp, next = node.right, node.left
        
        node.right = prev
        node.left = prev_l
        
        if not next:
            return node
        else:
            return traverse(next, node, temp)
        
    return traverse(root, None, None)