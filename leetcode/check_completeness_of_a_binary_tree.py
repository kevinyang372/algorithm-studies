# Given a binary tree, determine if it is a complete binary tree.

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

def isCompleteTree(root):
    if not root: return True
    
    stack = [[root, 0]]
    cur_level = 0
    count = 0
    prev = True
    
    while stack:
        
        node, level = stack.pop(0)
        
        if level > cur_level:
            if count < 2 ** cur_level:
                return False
            count = 0
            cur_level += 1
            prev = True
        
        count += 1
        
        if node.left and node.right:  
            if not prev:
                return False
            stack.append([node.left, level + 1])
            stack.append([node.right, level + 1])
        elif not node.right:
            if node.left:
                if not prev:
                    return False
                stack.append([node.left, level + 1])
            prev = False
        else:
            return False
        
    return True