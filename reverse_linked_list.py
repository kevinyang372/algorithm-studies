# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList_recursive(head):

    if head is None:
        return None

    fulllist = reverseList(head)

    return fulllist[0]

def reverseList(head):

    if head.next == None:
        return [head]

    temp = reverseList(head.next)
    temp[-1].next = head
    head.next = None
    temp.append(head)

    return temp

# iterative
def reverseList(head):
    if not head: return
    
    posterior = head.next
    prior = None
    
    while posterior:
        temp = posterior.next
        head.next = prior
        
        prior = head
        head = posterior
        posterior = temp
        
    head.next = prior
    return head