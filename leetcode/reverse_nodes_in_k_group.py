# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):

    if k == 1: return head

    cur = head
    t = k
    while t > 0:
        if not cur:
            return head
        cur = cur.next
        t -= 1

    t0, t1 = None, head
    while t1 != cur:
        temp = t1.next
        t1.next = t0
        t1, t0 = temp, t1

    head.next = self.reverseKGroup(cur, k)
    return t0
