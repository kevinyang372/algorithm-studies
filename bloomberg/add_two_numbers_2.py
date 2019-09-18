# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

def addTwoNumbers(self, l1, l2):
        
    s1, s2 = [], []
    node1, node2 = l1, l2
    
    while node1:
        s1.append(node1.val)
        node1 = node1.next
    
    while node2:
        s2.append(node2.val)
        node2 = node2.next
        
    res = None
    extra = 0
    
    while s1 or s2:
        
        if s1:
            v1 = s1.pop()
        else:
            v1 = 0
            
        if s2:
            v2 = s2.pop()
        else:
            v2 = 0
        
        val = (v1 + v2 + extra) % 10
        extra = (v1 + v2 + extra) // 10
        
        temp = ListNode(val)
        res, temp.next = temp, res
    
    if extra:
        temp = ListNode(extra)
        res, temp.next = temp, res
        
    return res