# Given two (singly) linked lists, determine if the two lists intersect. Return the inter- secting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def intersection(head1, head2):

    if not head1 or not head2: return False

    origin = head1

    while head1.next:
        head1 = head1.next

    head1.next = head2

    fast = slow = origin

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

        if fast == slow:
            fast = origin
            while fast != slow:
                fast, slow = fast.next, slow.next
            return fast

    return False