# Given a 32-bit signed integer, reverse digits of an integer.

def reverse_integer(inp):

    if inp < 0:
        is_negative = True
        inp = -inp
    else:
        is_negative = False

    digits = []

    while inp != 0:
        digits.append(int(inp % 10))
        inp = int(inp / 10)

    print(digits)

    new_inp = 0
    for i in range(len(digits)):
        new_inp += digits[i] * 10 ** (len(digits) - i - 1)

    return -new_inp if is_negative else new_inp

def reverse(x):
    if x < 0:
        return -reverse(-x)
    
    temp = []
    while x > 0:
        temp.append(x % 10)
        x //= 10
    
    res = sum([v * 10 ** i for i, v in enumerate(temp[::-1])])
    return res if res < 2**31 else 0