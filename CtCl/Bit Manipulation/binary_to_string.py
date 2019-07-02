# Binary to String: Given a real number between 8 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR:'

def printBinary(num):

    if num <= 0 or num >= 1: return "ERROR"
    init = '0.'
    count = -1

    while num:
        if len(init) > 32:
            return "ERROR"

        if num < 2 ** count:
            init += '0'
        else:
            num -= 2 ** count
            init += '1'
            
        count -= 1

    return init