# Sort a linked list using insertion sort.


# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

def insertionSortList(self, head):
        
    if not head: return
    
    def unlinkNode(node):
        if not node.prev:
            node.next.prev = None
        elif not node.next:
            node.prev.next = None
        else:
            node.prev.next, node.next.prev = node.next, node.prev
        node.next = None
        node.prev = None
    
    def insert(node, pos):
        if pos.next:
            pos.next.prev = node
        node.prev = pos
        node.next, pos.next = pos.next, node
           
    i, t = None, head
    while t:
        t.prev = i
        i, t = t, t.next
    
    start = head.next
    while start:
        temp = start.next
        prev = start.prev
        
        unlinkNode(start)
        while prev:
            if start.val < prev.val:
                prev = prev.prev
            else:
                break
        
        if not prev:
            head, start.next= start, head
            head.next.prev = head
        else:
            insert(start, prev)
        
        start = temp
    
    return head

def insertionSortList(self, head: ListNode) -> ListNode:
    if not head: return
    prev, node = head, head.next
    
    while node:
        next = node.next
        prev.next = None
        
        i, j = None, head
        while j and j.val < node.val:
            i, j = j, j.next
            
        if i:
            i.next = node
        else:
            head = node
        
        if j:
            node.next = j
            
            while j.next:
                j = j.next
            
            j.next = next
            prev = j
        else:
            node.next = next
            prev = node
            
        node = next
    
    return head