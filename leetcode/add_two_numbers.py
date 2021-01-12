# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = node = None
    carry_over = 0

    while l1 and l2:

        temp_sum = l1.val + l2.val + carry_over
        if temp_sum >= 10:
            carry_over = temp_sum // 10
            temp_sum %= 10
        else:
            carry_over = 0

        if not head:
            head = node = ListNode(temp_sum)
        else:
            node.next = ListNode(temp_sum)
            node = node.next

        l2 = l2.next
        l1 = l1.next

    rest = l1 if l1 else l2

    while rest:
        temp_sum = rest.val + carry_over
        if temp_sum >= 10:
            carry_over = temp_sum // 10
            temp_sum %= 10
        else:
            carry_over = 0

        if not head:
            head = node = ListNode(temp_sum)
        else:
            node.next = ListNode(temp_sum)
            node = node.next

        rest = rest.next

    if carry_over:
        node.next = ListNode(carry_over)

    return head
