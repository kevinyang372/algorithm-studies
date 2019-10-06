# Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

# The returned string must have no leading zeroes, unless the string is "0".

def baseNeg2(N):

    if N == 0 or N == 1: return str(N)
    
    return baseNeg2(-(N >> 1)) + str(N & 1)