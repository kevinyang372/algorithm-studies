# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):

    if not lists: return

    stack = [(i.val, i) for i in lists if i]

    heapq.heapify(stack)
    res = None
    head = None

    while stack:
        value, ind = heapq.heappop(stack)

        if ind.next:
            heapq.heappush(stack, (ind.next.val, ind.next))

        if res: 
            res.next = ind
        else:
            head = ind

        res = ind

    return head