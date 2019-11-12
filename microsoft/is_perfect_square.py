# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false

# binary search
def isPerfectSquare(self, num):
    if num == 1: return True
    
    start, end = 1, num
    
    while start < end:
        mid = (start + end) // 2
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            end = mid
        else:
            start = mid + 1
            
    return False