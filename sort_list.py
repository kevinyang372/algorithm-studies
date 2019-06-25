# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def sortList(self, head):

    if not head or not head.next: return head

    pivot = head
    head = head.next

    less = None
    less_head = None

    more = None
    more_head = None

    equal = pivot

    while head:

        if head.val < pivot.val:
            if not less:
                less = head
                less_head = head
            else:
                less.next = head
                less = less.next
        elif head.val > pivot.val:
            if not more:
                more = head
                more_head = head
            else:
                more.next = head
                more = more.next
        else:
            equal.next = head
            equal = equal.next

        head = head.next

    if less: less.next = None
    if more: more.next = None
    
    ls = sortList(less_head)
    mr = sortList(more_head)

    if ls:
        new_head = ls
        while ls.next:
            ls = ls.next
        ls.next = pivot
    else:
        new_head = pivot

    equal.next = mr

    return new_head



