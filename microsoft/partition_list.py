# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

def partition(self, head, x):
        
    if not head: return
    
    head_s = tail_s = head_l = tail_l = None
    
    while head:
        if head.val < x:
            if not head_s:
                head_s = tail_s = head
            else:
                tail_s.next = head
                tail_s = head
        else:
            if not head_l:
                head_l = tail_l = head
            else:
                tail_l.next = head
                tail_l = head
                
        head = head.next
       
    if tail_s:
        tail_s.next = head_l
    else:
        head_s = head_l
        
    if tail_l:
        tail_l.next = None
        
    return head_s