# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

def minDepth(self, root):
    if not root: return 0
    
    q = collections.deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        
        if not node.left and not node.right:
            return depth
        
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))

    return

# DFS
def minDepth(self, root: TreeNode) -> int:
    if not root: return 0
    if not root.left and not root.right: return 1
    
    left = right = float('inf')
    if root.left:
        left = self.minDepth(root.left) + 1
    if root.right:
        right = self.minDepth(root.right) + 1
        
    return min(left, right)