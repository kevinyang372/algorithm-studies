# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

# After doing so, return the head of the final linked list.  You may return any such answer.

 

# (Note that in the examples below, all sequences are serializations of ListNode objects.)

# Example 1:

# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
# Example 2:

# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# Example 3:

# Input: head = [1,2,3,-3,-2]
# Output: [1]
 

# Constraints:

# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.

def removeZeroSumSublists(self, head):
    sums = []
    t = head
    
    while t:
        temp = []
        ind = -1
        for i, (val, node) in enumerate(sums):
            new_val = val + t.val
            if new_val == 0 and ind < 0:
                ind = i
            temp.append((new_val, node))
        
        if t.val == 0 and ind < 0:
            ind = len(temp)
            
        temp.append((t.val, t))
        
        if ind < 0:
            sums = temp
        else:
            if ind == 0:
                head = t.next
                sums = []
            else:
                sums[ind - 1][1].next = t.next
                sums = temp[:ind]
                
        t = t.next
    
    return head