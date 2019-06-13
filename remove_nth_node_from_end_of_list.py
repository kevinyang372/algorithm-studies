# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):

    if not head.next: 
        return None
    elif n == 1:
        tail = head
        while tail.next and tail.next.next:
            tail = tail.next
        tail.next = None
        
        return head
    
    fast = prev = head
    step = n

    count = 0
    length = 0
    
    while True:

        counter = 0
        temp = fast

        while counter < step:
            
            if not fast:
                break
            
            fast = fast.next
            counter += 1
            length += 1
        
        if counter == step and fast:
            prev = temp
        else:
            count = counter
            break

    temp = 1
    while temp < count:
        prev = prev.next
        temp += 1
        
    if n == length:
        head = head.next
    else:
        prev.next = prev.next.next

    return head
