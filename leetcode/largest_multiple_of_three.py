# Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

# Since the answer may not fit in an integer data type, return the answer as a string.

# If there is no answer return an empty string.

 

# Example 1:

# Input: digits = [8,1,9]
# Output: "981"
# Example 2:

# Input: digits = [8,6,7,1,0]
# Output: "8760"
# Example 3:

# Input: digits = [1]
# Output: ""
# Example 4:

# Input: digits = [0,0,0,0,0,0]
# Output: "0"
 

# Constraints:

# 1 <= digits.length <= 10^4
# 0 <= digits[i] <= 9
# The returning answer must not contain unnecessary leading zeros.

def largestMultipleOfThree(self, digits: List[int]) -> str:
        
    remainder = sum(digits) % 3
    digits.sort(key = lambda x: -x)
    
    if remainder == 0:
        temp = "".join(map(str, digits))
        if not temp: return temp
        return str(int(temp))
    
    elif remainder == 1:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] % 3 == 1:
                digits.pop(i)
                temp = "".join(map(str, digits))
                if not temp: return temp
                return str(int(temp))
            
        c = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] % 3 == 2:
                digits.pop(i)
                c += 1
            if c == 2:
                temp = "".join(map(str, digits))
                if not temp: return temp
                return str(int(temp))
            
    elif remainder == 2:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] % 3 == 2:
                digits.pop(i)
                temp = "".join(map(str, digits))
                if not temp: return temp
                return str(int(temp))
            
        c = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] % 3 == 1:
                digits.pop(i)
                c += 1
            if c == 2:
                temp = "".join(map(str, digits))
                if not temp: return temp
                return str(int(temp))
        
    return ""