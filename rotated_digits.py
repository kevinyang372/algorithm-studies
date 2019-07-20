# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

# Now given a positive number N, how many numbers X from 1 to N are good?

# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:

# N  will be in range [1, 10000].

# using sets
def rotatedDigits(N):
        
    notvalid = set([0,1,8])
    all_pool = set([0,1,2,5,6,8,9])
    
    num = 0
    for i in range(1, N + 1):
        temp = set([int(t) for t in str(i)])
        
        if temp.issubset(all_pool) and not temp.issubset(notvalid):
            num += 1
            
    return num

# using method of exclusion
def rotatedDigits(N):
    
    num = 0
    for i in range(1, N + 1):
        temp = str(i)
        
        if '3' in temp or '4' in temp or '7' in temp:
            continue
        if '2' in temp or '5' in temp or '6' in temp or '9' in temp:
            num += 1
            
    return num
