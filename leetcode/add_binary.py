# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(self, a, b):
        
    if len(a) > len(b):
        a, b = b, a
        
    extra = 0
    i, j = len(a) - 1, len(b) - 1
    res = ''
    
    while i >= 0:
        res = str((int(a[i]) + int(b[j]) + extra) % 2) + res
        extra = (int(a[i]) + int(b[j]) + extra) // 2
        i -= 1
        j -= 1
    
    if j >= 0:
        while j >= 0:
            res = str((int(b[j]) + extra) % 2) + res
            extra = (int(b[j]) + extra) // 2
            j -= 1
            
    if extra == 1:
        res = '1' + res
        
    return res