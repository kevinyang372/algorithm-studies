# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
# DEFINI TION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -) B -) C -) 0 -) E -) C[thesameCasearlierl Output: C

def detect_loop(head):

    fast = slow = head

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

        if fast == slow:
            fast = head
            while fast != slow:
                fast, slow = fast.next, slow.next
            return fast

    return False