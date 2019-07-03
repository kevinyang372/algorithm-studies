# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

def levelOrder(root):

    if not root: return

    stack = [(root, 1)]
    res = []

    while stack:
        node, level = stack.pop(0)

        if len(res) < level:
            res.append([node.val])
        else:
            res[level].append(node.val)

        if node.left:
            stack.append((node.left, level + 1))

        if node.right:
            stack.append((node.right, level + 1))

    return res