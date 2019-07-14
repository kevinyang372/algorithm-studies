# Write a function to swap a number in place (that is, without temporary variables).

# e.g. a = 5, b = 3
def swap(a, b)
    
    a = a + b # a = 5 + 3 = 8
    b = a - b # b = 8 - 3 = 5
    a = a - b # a = 8 - 5 = 3

    return a, b