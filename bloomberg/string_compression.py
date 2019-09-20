# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.

 
# Follow up:
# Could you solve it using only O(1) extra space?

 
# Example 1:

# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

# Example 2:

# Input:
# ["a"]

# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]

# Explanation:
# Nothing is replaced.
 

# Example 3:

# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.
 

# Note:

# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.

def compress(self, chars):
        
    if len(chars) < 2: return len(chars)
    
    i, j = 0, 1
    pre = 0
    count = 0
    
    while j < len(chars) + 1:
        while j < len(chars) and chars[i] == chars[j]:
            j += 1
        
        chars[pre] = chars[i]
        if j - i > 1:
            temp = []
            num = j - i
            while num > 0:
                temp = [str(num % 10)] + temp
                num //= 10
            
            chars[pre + 1: pre + 1 + len(temp)] = temp
            pre += len(temp) + 1
            count += len(temp) + 1
        else:
            pre += 1
            count += 1
            
        i, j = j, j + 1
    
    
    return count