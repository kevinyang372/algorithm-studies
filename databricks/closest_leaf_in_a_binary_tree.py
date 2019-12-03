# Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

# Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

# In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

# Example 1:

# Input:
# root = [1, 3, 2], k = 1
# Diagram of binary tree:
#           1
#          / \
#         3   2

# Output: 2 (or 3)

# Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
# Example 2:

# Input:
# root = [1], k = 1
# Output: 1

# Explanation: The nearest leaf node is the root node itself.
# Example 3:

# Input:
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Diagram of binary tree:
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6

# Output: 3
# Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
# Note:
# root represents a binary tree with at least 1 node and at most 1000 nodes.
# Every node has a unique node.val in range [1, 1000].
# There exists some node in the given binary tree for which node.val == k.

def findClosestLeaf(self, root, k):
        
    def findNode(node):
        if node.val == k: return node
        
        if node.left:
            node.left.parent = node
            res = findNode(node.left)
                
            if res: return res
        
        if node.right:
            node.right.parent = node
            res = findNode(node.right)
            
            if res: return res
        
        return None
    
    root.parent = None
    key = findNode(root)
    cache = {}
    
    def checkMinDepth(node):
        if not node.left and not node.right: return 1, node.val
        if node in cache: return cache[node]
        
        dl = dr = float('inf')
        if node.left:
            dl, nl = checkMinDepth(node.left)
        
        if node.right:
            dr, nr = checkMinDepth(node.right)
        
        if dl < dr:
            cache[node] = (dl + 1, nl)
            return dl + 1, nl
        else:
            cache[node] = (dr + 1, nr)
            return dr + 1, nr
        
    res = [float('inf'), None]
    dis = 0
    while key:
        temp, node = checkMinDepth(key)
        if temp + dis < res[0]:
            res[1] = node
            res[0] = temp
        dis += 1
        key = key.parent
        
    return res[1]