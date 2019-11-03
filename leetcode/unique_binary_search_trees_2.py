# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:

# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

def generateTrees(self, n):
    if n == 0: return
    cache = {}
    def traverse(arr):
        if not arr: return [None]
        if len(arr) == 1: return [TreeNode(arr[0])]
        if tuple(arr) in cache: return cache[tuple(arr)]
        
        res = []
        for i in range(len(arr)):
            
            lefts = traverse(arr[:i])
            rights = traverse(arr[i + 1:])
            
            for m in lefts:
                for n in rights:
                    root = TreeNode(arr[i])
                    root.left = m
                    root.right = n
                    res.append(root)
            
        cache[tuple(arr)] = res
        return res
    
    return traverse([i for i in range(1, n + 1)])