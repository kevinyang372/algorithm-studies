# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

# Return the largest string X such that X divides str1 and X divides str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Note:

# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.

def gcdOfStrings(str1, str2):
        
    if not str1 or not str2: return ''
    if str1 == str2: return str1
    
    i = 0
    temp = ''
    res = ''
    
    while i < len(str1) and i < len(str2):
        if str1[i] != str2[i]:
            break
        
        temp += str1[i]
        if str1.count(temp) * len(temp) == len(str1) and str2.count(temp) * len(temp) == len(str2):
            res = temp
        
        i += 1
    
    return res

# O(N + M) Solution
def gcdOfStrings(str1, str2):

    if len(str1) == len(str2):
        return str1 if str1 == str2 else ''
    else:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1[:len(str2)] == str2:
            return gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
