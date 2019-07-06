# Write a recursive function to multiply two positive integers without using the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

def recursiveMultiply(num1, num2):
    if num1 == 0 or num2 == 0: return 0
    return num1 + recursiveMultiply(num1, num2 - 1)

# better
def recursiveMultiply(num1, num2):
    if num1 == 0 or num2 == 0: return 0
    smaller = num1 if num1 < num2 else num2
    bigger = num2 if num1 < num2 else num1

    return bigger + recursiveMultiply(bigger, smaller - 1)