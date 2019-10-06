# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):

    if not l1 and not l2: return

    if l1 and l2:
        b, s = (l1, l2) if l1.val < l2.val else (l2, l1)

        node = ListNode(b.val)
        node.next = mergeTwoLists(b.next, s)

        return node
    else:
        return l1 if l1 else l2