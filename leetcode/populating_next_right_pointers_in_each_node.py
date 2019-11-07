# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example:



# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 

# Note:

# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.

# recursive, O(h)
def connect(self, root):
    if not root: return
    
    def helper(node):
        if not node.left or not node.right: return [], []
        
        node.left.next = node.right
        
        l1, r1 = helper(node.right)
        l2, r2 = helper(node.left)
        
        for i in range(len(l1)):
            r2[i].next = l1[i]
            
        return l2 + [node.left], r1 + [node.right]
        
    helper(root)
    return root

# recursive
def connect(self, root):
        
    def traverse(node):
        if not node: return
        
        prev = None
        head = None
        
        while node:
            if node.left:
                if prev:
                    prev.next = node.left
                if not head:
                    head = node.left
                prev = node.left
            if node.right:
                if prev:
                    prev.next = node.right
                if not head:
                    head = node.right
                prev = node.right
            node = node.next
        
        traverse(head)
    
    traverse(root)
    return root

# iterative
def connect(self, root):
    head = root
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            if root.next: root.right.next = root.next.left
            root = root.next
        root = next
    return head