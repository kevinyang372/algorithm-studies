# A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

# Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

 

# Example 1:

# Input: num = "257"
# Output: "IOI"
# Explanation:  257 is 101 in hexadecimal.
# Example 2:

# Input: num = "3"
# Output: "ERROR"

def toHexspeak(self, num):
    num = int(num)
    res = []
    
    d = {
        0: "O",
        1: "I",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    
    t = int(math.log(num, 16))
    while t > -1:
        temp = num // 16 ** t
        if temp not in d: return "ERROR"
        res.append(d[temp])
        num %= 16 ** t
        t -= 1
    
    return "".join(res)