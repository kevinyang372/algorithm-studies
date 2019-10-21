# Given an input string , reverse the string word by word. 

# Example:

# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note: 

# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# Follow up: Could you do it in-place without allocating extra space?

# O(1) in space
def reverseWords(self, s):
        
    def reverse(start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    reverse(0, len(s) - 1)
    i = j = 0
    
    while j < len(s):
        while j < len(s) and s[j] != " ":
            j += 1
        reverse(i, j - 1)
        
        j += 1
        i = j
    
    return s