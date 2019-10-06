# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

def multiply(self, num1, num2):
    n1 = num1 if len(num1) <= len(num2) else num2
    n2 = num2 if len(num1) <= len(num2) else num1

    if len(n1) == 1:
        
        key = int(n1)
        if key == 0: return "0"
        if key == 1: return n2
        
        t = len(n2) - 1
        over = 0
        res = 0
        
        while t > -1:
            temp = key * int(n2[t]) + over 
            res += (temp % 10) * 10 ** (len(n2) - 1 - t)
            over = temp // 10
            t -= 1
        
        if over > 0:
            res += over * 10 ** (len(n2) - 1 - t)
        
        return str(res)
    else:
        t = len(n1) - 1
        res = 0
        
        while t > -1:
            res += int(self.multiply(n1[t], n2)) * 10 ** (len(n1) - 1 - t)
            t -= 1
            
        return str(res)