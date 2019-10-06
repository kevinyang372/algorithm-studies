# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head):

    slow = fast = head
    prev = None

    while fast and fast.next:
        temp = slow
        slow, fast = slow.next, fast.next.next
        temp.next, prev = prev, temp

    if fast:
        slow = slow.next

    while prev and slow:
        if prev.val != slow.val:
            return False

        prev, slow = prev.next, slow.next

    return True





