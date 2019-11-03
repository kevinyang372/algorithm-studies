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
def zigzagLevelOrder(self, root):
    if not root: return
    res = []
    stack = [root]
    l2r = True
    
    while stack:
        temp = []
        curr = []
        for i in range(len(stack)):
            curr.append(stack[i].val)
            if stack[i].left:
                temp.append(stack[i].left)
            if stack[i].right:
                temp.append(stack[i].right)
        
        if l2r:
            res.append(curr)
            l2r = False
        else:
            res.append(curr[::-1])
            l2r = True
            
        stack = temp
            
    return res