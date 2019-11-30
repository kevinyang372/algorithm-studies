# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

# Each node of each tree in the answer must have node.val = 0.

# You may return the final list of trees in any order.

 

# Example 1:

# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:

 

# Note:

# 1 <= N <= 20

def allPossibleFBT(self, N):
        
    if N == 1: return [TreeNode(0)]
    if N % 2 == 0: return []
    
    res = []
    for i in range(1, N - 1, 2):
        for left in self.allPossibleFBT(i):
            for right in self.allPossibleFBT(N - i - 1):
                root = TreeNode(0)
                root.left = left
                root.right = right
                res.append(root)
    return res