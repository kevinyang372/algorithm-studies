# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:

    if not head:
        return None

    counter = 1

    flip_head = None
    flip_tail = None

    node = head
    while counter <= n:
        if counter == m - 1:
            flip_head = node
        elif counter == n:
            flip_tail = node
            break

        counter += 1
        node = node.next

    if m == 1:
        reverseList(head, flip_tail)
        head.next = flip_tail.next
        head = flip_tail
    else:
        temp = flip_tail.next
        reverseList(flip_head.next, flip_tail)
        flip_head.next.next = temp
        flip_head.next = flip_tail

    return head


def reverseList(head, tail):

    previous_node = head.next
    head.next = None
    
    while previous_node != tail:

        temp = previous_node.next
        previous_node.next = head

        head = previous_node
        previous_node = temp

    previous_node.next = head