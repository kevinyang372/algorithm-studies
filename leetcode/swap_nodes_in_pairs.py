# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

 

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

def swapPairs(self, head: ListNode) -> ListNode:
        
    if not head: return
    if not head.next: return head
    
    i, j = head, head.next
    
    def traverse(i, j):
        if not i or not j: return i
        
        next = j.next
        j.next = i
        
        if next:
            i.next = traverse(next, next.next)
        else:
            i.next = None
            
        return j
    
    return traverse(i, j)
        