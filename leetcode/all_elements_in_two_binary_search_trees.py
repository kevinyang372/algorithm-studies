# Given two binary search trees root1 and root2.

# Return a list containing all the integers from both trees sorted in ascending order.

 

# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:

# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]
# Example 3:

# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]
# Example 4:

# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]
# Example 5:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
 

# Constraints:

# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].

def getAllElements(self, root1, root2):
        
    def getSuccessor(node):
        if node.right:
            next = node.right
            next.parent = node
            
            while next.left:
                next.left.parent = next
                next = next.left
            
            return next
        else:
            while node.parent and node.parent.val < node.val:
                node = node.parent
            return node.parent
        
    r1, r2 = root1, root2
    
    if r1: r1.parent = None
    if r2: r2.parent = None
    
    while r1 and r1.left:
        r1.left.parent = r1
        r1 = r1.left
    
    while r2 and r2.left:
        r2.left.parent = r2
        r2 = r2.left
        
    res = []
    while r1 or r2:
        if not r1:
            res.append(r2.val)
            r2 = getSuccessor(r2)
        elif not r2:
            res.append(r1.val)
            r1 = getSuccessor(r1)
        elif r1.val < r2.val:
            res.append(r1.val)
            r1 = getSuccessor(r1)
        else:
            res.append(r2.val)
            r2 = getSuccessor(r2)
            
    return res