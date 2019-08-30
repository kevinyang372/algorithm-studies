# We are given a binary tree (with root node root), a target node, and an integer value K.

# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

# Output: [7,4,1]

# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.



# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
 

# Note:

# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.

def distanceK(self, root, target, K):
        
    def traverse(node):
        
        k = collections.defaultdict(list)
        k[0].append(node.val)
        t = 'None'
        res = []
        dis = -1
        distance_l, distance_r = None, None
        
        if node == target:
            t = 'current'
            dis = 0
        
        if node.left:
            distance_l, has_target, d = traverse(node.left)
            if d > 0:
                t = 'left'
                res += has_target
                dis = d
                
        if node.right:
            distance_r, has_target, d = traverse(node.right)
            if d > 0:
                t = 'right'
                res += has_target
                dis = d
        
        if t == 'right':
            if distance_l:
                for i in distance_l:
                    k[i + 1] += distance_l[i]
            res += k[K - dis]
            if distance_r:
                for i in distance_r:
                    k[i + 1] += distance_r[i]
        elif t == 'left':
            if distance_r:
                for i in distance_r:
                    k[i + 1] += distance_r[i]
            res += k[K - dis]
            if distance_l:
                for i in distance_l:
                    k[i + 1] += distance_l[i]
        else:
            if distance_r:
                for i in distance_r:
                    k[i + 1] += distance_r[i]
            if distance_l:
                for i in distance_l:
                    k[i + 1] += distance_l[i]
            if t == 'current':
                res += k[K]
        
        return k, res, dis + 1
    
    return traverse(root)[1]