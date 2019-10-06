# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

def addStrings(num1, num2):

    res = 0
    count = 0

    while num1 and num2:
        res += (int(num1[-1]) + int(num2[-1])) * 10 ** count

        num1 = num1[:-1]
        num2 = num2[:-1]

        count += 1

    if not num1 and not num2: return str(res)

    temp = num1 if num1 else num2

    while temp:
        res += int(temp[-1]) * 10 ** count
        temp = temp[:-1]
        count += 1

    return str(res)

