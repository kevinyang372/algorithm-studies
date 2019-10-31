# Given edges : {{'a','b'}, {'a','d'}, {'b','c'}} ,Contruct a binary tree.
# Explain: {parent, child} , {a ,b} , b's parent node is a.

# Tree :

#             a
#       b          d
#     c

import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def createTree(lis):
    degree = collections.defaultdict(int)
    d = {}
    
    for x, y in lis:
        if x not in d:
            d[x] = TreeNode(x)

        if y not in d:
            d[y] = TreeNode(y)

        if not d[x].left:
            d[x].left = d[y]
        else:
            d[x].right = d[y]
            
        degree[y] += 1
        
    for i in d:
        if degree[i] == 0:
            return d[i]
    
    return