# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted linked list: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

def sortedListToBST(self, head):
    if not head: return
    
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow, fast = slow.next, fast.next.next
        
    if slow == fast:
        return TreeNode(slow.val)
    
    root = TreeNode(slow.val)
    prev.next = None
    
    root.right = self.sortedListToBST(slow.next)
    root.left = self.sortedListToBST(head)
    
    return root