# Remove Dups: Write code to remove duplicates from an unsorted li nked list. FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# With buffer
def remove_dups(lis):

    if lis is None: return

    buff = [lis.val]

    while lis.next:
        if lis.next.val in buff:
            lis.next = lis.next.next
        else:
            buff.append(lis.next.val)

    return lis

# Without buffer
def remove_dups(lis):

    if lis is None: return

    current = lis

    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next 

    return lis