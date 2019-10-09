# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with same node values.

# Example 1:

#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:

#       2
#      /
#     4
# and

#     4
# Therefore, you need to return above trees' root in the form of a list.

def findDuplicateSubtrees(self, root):
        
    d = {}
    res = []
    
    def dfs(node):
        if not node: return "#"
        
        key = node.val
        right = dfs(node.right)
        left = dfs(node.left)
        
        temp = 'l:' + left + str(key) + 'r:' + right
        if temp in d and d[temp]:
            res.append(node)
            d[temp] = False
        elif temp not in d:
            d[temp] = True
    
        return temp
    
    dfs(root)
    return res