# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

# Example :

# Input: [1,2,3]
# Output: [1,2,4]

def plusOne(self, head):
        
    def add(node):
        if node.next:
            _, plus = add(node.next)
        else:
            plus = 1
        
        if node.val + plus > 9:
            node.val = 0
            return node, 1
        else:
            node.val = node.val + plus
            return node, 0
    
    node, plus = add(head)
    if plus == 1:
        newhead = ListNode(1)
        newhead.next = node
        return newhead
    else:
        return node