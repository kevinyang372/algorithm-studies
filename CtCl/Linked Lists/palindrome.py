# Implement a function to check if a linked list is a palindrome

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head):

    if not head: return True

    slow = fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.val)
        slow, fast = slow.next, fast.next.next

    if fast:
        slow = slow.next

    while slow:
        node = stack.pop()

        if slow.val != node:
            return False

    return True