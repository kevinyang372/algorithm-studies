# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:

# Input: [3,9,20,null,null,15,7]

#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 

# Output:

# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:

# Input: [3,9,8,4,0,1,7]

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7 

# Output:

# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:

# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2

# Output:

# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

def verticalOrder(self, root):
    if not root: return
    d = collections.defaultdict(list)
    
    queue = collections.deque([(root, 0)])
    min_val = max_val = 0
    
    while queue:
        node, pos = queue.popleft()
        d[pos].append(node.val)
        
        if pos < 0:
            min_val = min(min_val, pos)
        else:
            max_val = max(max_val, pos)
        
        if node.left:
            queue.append((node.left, pos - 1))
        if node.right:
            queue.append((node.right, pos + 1))
       
    res = []
    for i in range(min_val, max_val + 1):
        if i in d:
            res.append(d[i])
            
    return res
    