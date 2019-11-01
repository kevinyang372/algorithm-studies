# Deep copy of an N-ary tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def copyNAry(root):
    d = {}

    def traverse(node):
        if node in d:
            new = d[node]
        else:
            new = TreeNode(node.val)
            d[node] = new

        for child in node.children[::-1]:
            new.children.append(traverse(child))

        return new

    return traverse(root)
