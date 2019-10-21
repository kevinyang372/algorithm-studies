# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

# Note:

# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Example:

# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

#     4
#    / \
#   2   5
#  / \
# 1   3

# Output: [4,3]
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

def closestKValues(self, root, target, k):
        
    root.parent = None
    
    def search(node, lower, upper):
        if not node: return (lower, upper)
        if node.val > target:
            if node.left:
                node.left.parent = node
            if upper:
                upper = min(upper, node, key=lambda x: x.val)
            else:
                upper = node
            return search(node.left, lower, upper)
        else:
            if lower:
                lower = max(lower, node, key=lambda x: x.val)
            else:
                lower = node
            if node.right:
                node.right.parent = node
            return search(node.right, lower, upper)
    
    lower, upper = search(root, None, None)
    
    stack = []
    res = []
    
    if lower:
        heapq.heappush(stack, (abs(lower.val - target), lower))
    if upper:
        heapq.heappush(stack, (abs(upper.val - target), upper))
    
    def findSuccessor(node):
        if node.right:
            temp = node.right
            temp.parent = node
            while temp.left:
                temp.left.parent = temp
                temp = temp.left
            return temp
        else:
            current = node
            while current.parent:
                if current.parent.val > current.val:
                    return current.parent
                else:
                    current = current.parent
            return None
        
    def findPredecessor(node):
        if node.left:
            temp = node.left
            temp.parent = node
            while temp.right:
                temp.right.parent = temp
                temp = temp.right
            return temp
        else:
            current = node
            while current.parent:
                if current.parent.val < current.val:
                    return current.parent
                else:
                    current = current.parent
            return None
    
    while stack and len(res) < k:
        _, node = heapq.heappop(stack)
        res.append(node.val)
        
        if node.val > target:
            n = findSuccessor(node)
        else:
            n = findPredecessor(node)
            
        if n is not None:
            heapq.heappush(stack, (abs(n.val - target), n))
    
    return res