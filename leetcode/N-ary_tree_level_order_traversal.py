# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example, given a 3-ary tree:

 



 

# We should return its level order traversal:

# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
 

# Note:

# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

def levelOrder(self, root):
    if not root: return
    
    stack = collections.deque([(root, 0)])
    res = []
    
    while stack:
        node, level = stack.popleft()
        if len(res) < level + 1:
            res.append([node.val])
        else:
            res[level].append(node.val)
        
        for i in node.children:
            stack.append((i, level + 1))
    
    return res