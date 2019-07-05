# A magic index in an array A[e... n-1] is defined to be an index such that A[ i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

def findIndex(num):
    return findIndex_helper(num, 0, len(num) - 1)

    
def findIndex_helper(num, start, end):
    
    mid = (start + end) // 2
    if num[mid] == mid: return True

    if num[mid] > mid:
        return findIndex_helper(num, start, mid)
    else:
        return findIndex_helper(num, mid, end)
