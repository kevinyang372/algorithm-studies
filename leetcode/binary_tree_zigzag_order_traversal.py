# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# bfs
def zigzagLevelOrder(root):

    if not root: return
        
    queue = [root]
    res = []
    d = True
    
    while queue:
        temp = []
        vals = []
        
        if d:
            for i in range(len(queue)):
                if queue[-1 - i].right: temp.append(queue[-1 - i].right)
                if queue[-1 - i].left: temp.append(queue[-1 - i].left)
                vals.append(queue[i].val)
        else:
            for i in range(len(queue)):
                if queue[-1 - i].left: temp.append(queue[-i - 1].left)
                if queue[-1 - i].right: temp.append(queue[-i - 1].right)
                vals.append(queue[i].val)
        
        res.append(vals)
        queue = temp
        d = not d
    
    return res