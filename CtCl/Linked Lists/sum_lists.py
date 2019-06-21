# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-) 1 -) 6) + (5 -) 9 -) 2).Thatis,617 + 295. Output: 2 -) 1 -) 9.That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
# Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295. Output: 9 -) 1 -) 2.That is, 912

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def sum_lists_backward(head1, head2):

    if not head1: return head2
    if not head2: return head1

    re = 0
    res = None
    head = None

    while head1 or head2:

        if head1:
            if head2:
                temp = head1.val + head2.val + re
                head1, head2 = head1.next, head2.next
            else:
                temp = head1.val + re
                head1 = head1.next
        else:
            temp = head2.val + re
            head2 = head2.next

        re = temp // 10
        node = ListNode(temp % 10)

        if res:
            res.next = node
        else:
            head = node

        res = node

    if re > 0: res.next = ListNode(re)

    return head

def reverse(head):

    tail = None
    while head:
        temp = head.next
        head.next = tail
        tail = head
        head = temp

    return tail      

def sum_lists_forward(head1, head2):

    if not head1: return head2
    if not head2: return head1

    head1 = reverse(head1)
    head2 = reverse(head2)

    return sum_lists_backward(head1, head2)
