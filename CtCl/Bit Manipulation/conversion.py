# Conversion: Write a function to determine the number of bits you would need to flip to convert integer A to integer B.

# EXAMPLE
# Input: 29 (or: 11101), 15 (or: (1111) Output: 2

def conversion(num1, num2):

    count = 0

    while num1 and num2:
        if (num1 & 1) ^ (num2 & 1) == 1:
            count += 1

        num1 = num1 >> 1
        num2 = num2 >> 1

    temp = num1 if num2 == 0 else num1

    while temp:
        if temp & 1 == 1:
            count += 1
        temp = temp >> 1

    return count

# better approach: use xor and count number of 1

def conversion(num1, num2):

    temp = num1 ^ num2
    count = 0

    while temp:
        if temp & 1 == 1:
            count += 1
        temp = temp >> 1

    return count