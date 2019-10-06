# Given an n-ary tree, return the preorder traversal of its nodes' values.

# For example, given a 3-ary tree:

 



 

# Return its preorder traversal as: [1,3,5,6,2,4].

 

# Note:

# Recursive solution is trivial, could you do it iteratively?
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# recursive
def preorder(self, root):
    if not root: return
    res = [root.val]
    for i in root.children:
        res += self.preorder(i)
    return res

# iterative
def preorder(self, root):
    if not root: return
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        stack += node.children[::-1]
    return res
            