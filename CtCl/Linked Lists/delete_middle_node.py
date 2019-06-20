# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f

def delete_middle_node(lis):

    fast = slow = lis

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    slow.next = slow.next.next
