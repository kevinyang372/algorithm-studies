# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):

    if not head or not head.next: return head
    
    pre, cur = head, head.next

    while cur:
        while cur and pre.val == cur.val:
            cur = cur.next
        pre.next = cur
        if not cur: break
        pre, cur = pre.next, cur.next

    return head