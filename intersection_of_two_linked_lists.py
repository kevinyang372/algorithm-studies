# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):

    if not headA or not headB: return None
    
    mat_a = []
    mat_b = []

    while headA:
        mat_a.append(headA)
        headA = headA.next

    while headB:
        mat_b.append(headB)
        headB = headB.next

    pre = None

    while mat_a and mat_b:

        temp_a = mat_a.pop()
        temp_b = mat_b.pop()

        if temp_a == temp_b:
            pre = temp_a
        else:
            break

    return pre

# O(N) time and O(1) space

def getIntersectionNode(headA, headB):

    if not headA or not headB: return None

    A = headA
    B = headB

    while A.next: A = A.next

    A.next = B

    fast = slow = headA

    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

        if fast == slow:
            fast = headA
            while fast != slow:
                fast, slow = fast.next, slow.next
            A.next = None
            return fast

    A.next = None
    return None


