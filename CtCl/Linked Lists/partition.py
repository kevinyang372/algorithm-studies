# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need to be after the elements less than x (see below).The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
# 2.4
# 94
# Cracking the Coding Interview, 6th Edition
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1[partition=5) Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 

def partition(lis, k):

    less = None
    more = None
    head = None

    while lis:
        if lis.val < k:
            if not less: 
                less = lis
                head = lis
            else: 
                less.next = lis
        else:
            if not more: 
                more = lis
            else:
                more.next = lis

    less.next = more
    more.next = None

    return head


