# Given a binary tree, return the vertical order traversal of its nodes values.

# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def verticalTraversal(root):

    if not root: return []

    d = {}

    stack = [(root, 0)]
    min_val = 0
    max_val = 0

    while stack:

        node, x = stack.pop(0)

        min_val = min(x, min_val)
        max_val = max(x, max_val)

        if node.right:
            stack.append((node.right, x + 1))

        if node.left:
            stack.append((node.left, x - 1))

        if x in d.keys():
            d[x].append(node.val)
        else:
            d[x] = [node.val]

    return [d[t] for t in range(min_val, max_val + 1)]