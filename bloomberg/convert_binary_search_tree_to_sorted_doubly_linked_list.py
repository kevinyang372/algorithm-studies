# Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

# Let's take the following BST as an example, it may help you understand the problem better:

 


 
# We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

 


 
# Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

# The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

class Solution(object):
    def __init__(self):
        self.smallest = None
        self.largest = None
        
    def treeToDoublyList(self, root):
        
        if not root: return
        
        def traverse(node):
            if not self.smallest or node.val < self.smallest.val:
                self.smallest = node
            if not self.largest or node.val > self.largest.val:
                self.largest = node
            if node.left:
                p = find_predecessor(node.left)
                traverse(node.left)
                
                node.left = p
                p.right = node
            
            if node.right:
                s = find_successor(node.right)
                traverse(node.right)
                
                node.right = s
                s.left = node
                
        def find_predecessor(node):
            if node.right:
                return find_predecessor(node.right)
            else:
                return node
        
        def find_successor(node):
            if node.left:
                return find_successor(node.left)
            else:
                return node
            
        
        traverse(root)
        self.smallest.left, self.largest.right = self.largest, self.smallest
        return self.smallest 
