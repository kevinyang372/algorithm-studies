# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

# Example:

# Input:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL

# Output:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL

def flatten(self, head):
    if not head: return
    
    def link(node):
        prev = None
        while node:
            if node.child:
                temp = node.next
                node.next, node.child.prev = node.child, node
                res = link(node.child)
                node.child = None
                if temp:
                    res.next, temp.prev = temp, res
                prev, node = res, temp
            else:
                prev, node = node, node.next 
        return prev
    
    link(head)
    return head