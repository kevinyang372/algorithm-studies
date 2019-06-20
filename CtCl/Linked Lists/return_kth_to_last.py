# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def kth_to_last(lis, k):

    if not lis or k <= 0: return

    fast = lis
    pre = None

    while True:

        temp = fast
        count = 1

        while fast.next:
            count += 1
            fast = fast.next

            if count >= k:
                break

        if count < k:
            if not pre: return 
            for i in range(k - count):
                pre = pre.next
                return pre
        else:
            pre = temp

# better approach

def kth_to_last(lis, k):

    runner = current = lis

    for _ in range(k):
        if not runner.next:
            return None
        runner = runner.next

    while runner:
        current, runner = current.next, runner.next

    return current