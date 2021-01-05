# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):

    if not head or not head.next:
        return head

    while head and head.next and head.val == head.next.val:
        temp = head.next
        while temp and temp.val == head.val:
            temp = temp.next
        head = temp

    if not head or not head.next: 
        return head
    else:
        head.next = self.deleteDuplicates(head.next)
        return head


# iterative
def deleteDuplicates(self, head: ListNode) -> ListNode:
    node = head
    node_distinct = root = None

    while node:
        if node.next and node.val == node.next.val:
            while node.next and node.val == node.next.val:
                node = node.next
            if node_distinct:
                node_distinct.next = None
        else:
            if not root:
                root = node
            if node_distinct:
                node_distinct.next = node
            node_distinct = node
        node = node.next

    return root
