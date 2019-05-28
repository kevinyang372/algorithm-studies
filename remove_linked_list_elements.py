# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head: ListNode, val: int):

    while head and head.val == val:
        head = head.next

    current_head = head
    
    if not head:
        return current_head

    while head.next:
        temp = head.next
        while temp and temp.val == val :
            temp = temp.next
            
        head.next = temp
        
        if not head.next:
            break
        
        head = head.next

    return current_head

