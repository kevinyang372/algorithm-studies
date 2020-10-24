# Given a TreeNode defined with an additional parent pointer, print all nodes of a given tree in any order using constant space. You are not allowed to modify the tree structure itself.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def traverse(node):

    prev = None
    while node:
        temp = node.val
        if node.left and node.left.val != prev and (not node.right or node.right.val != prev):
            node = node.left
        elif node.right and node.right.val != prev:
            node = node.right
        else:
            print(node.val)
            node = node.parent
        prev = temp

a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')

a.left, b.parent = b, a
b.right, c.parent = c, b
a.right, d.parent = d, a
d.left, e.parent = e, d

traverse(a)