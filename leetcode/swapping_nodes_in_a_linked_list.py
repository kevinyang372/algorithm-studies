# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).


# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
# Example 3:

# Input: head = [1], k = 1
# Output: [1]
# Example 4:

# Input: head = [1,2], k = 1
# Output: [2,1]
# Example 5:

# Input: head = [1,2,3], k = 2
# Output: [1,2,3]


# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100

def swapNodes(self, head: ListNode, k: int) -> ListNode:

    node = head
    i = 1
    n1 = n2 = None

    while node:
        if k == i:
            n1 = node
            n2 = head
        elif n2:
            n2 = n2.next
        node = node.next
        i += 1

    n1.val, n2.val = n2.val, n1.val
    return head
