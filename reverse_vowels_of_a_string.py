# Write a function that takes a string as input and reverse only the vowels of a string.
# 
# Example 1:
# 
# Input: "hello"
# Output: "holle"
# Example 2:
# 
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

def reverseVowels(self, s):
        
    chars = list(s)
    i, j = 0, len(s) - 1
    vows = ['a', 'e', 'i', 'o', 'u']

    while i < j:
        if chars[i].lower() in vows and chars[j].lower() in vows:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        elif chars[i].lower() in vows:
            j -= 1
        elif chars[j].lower() in vows:
            i += 1
        else:
            i += 1
            j -= 1

    return ''.join(chars)
        
