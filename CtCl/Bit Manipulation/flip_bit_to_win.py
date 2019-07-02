# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1syou could create.
# SOLUTION
# EXAMPLE
# Input: 1775 (or: 11011101111) Output: 8

def flipBit(num):

    max_count = 0
    count = 0

    while num:
        if num & 1:
            count += 1
        else:
            temp = num >> 1
            count += 1

            while temp & 1:
                count += 1
                temp = temp >> 1
            max_count = max(max_count, count)
            count = 0

        num = num >> 1

    max_count = max(max_count, count)

    return max_count

