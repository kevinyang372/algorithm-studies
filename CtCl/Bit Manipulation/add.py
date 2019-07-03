# Build the add function without using actual add

def add(num1, num2):

    if num1 & num2 == 0: return num1 ^ num2
    return add((num1 & num2) << 1, num1 ^ num2)


def subtract(num1, num2):

    if num2 == 0: return num1
    return subtract(num1 ^ num2, (~num1 & num2) << 1)