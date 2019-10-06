# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Examples:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

def decodeString(s):

    if len(s) < 3: return s
    
    res = ""
    ind_s = -1
    ind_e = -1
    i = 0

    while i < len(s):
        if s[i].isdigit():

            end = i + 1
            while s[end].isdigit():
                end += 1
            
            count = int(s[i:end])
            ind_s = end
            ind_e = end + 1
            
            stack = 1

            while stack > 0:
                if s[ind_e] == "[":
                    stack += 1
                elif s[ind_e] == "]":
                    stack -= 1

                ind_e += 1

            for i in range(count):
                res += decodeString(s[ind_s + 1:ind_e - 1])

            i = ind_e
        else:
            res += s[i]
            i += 1

    return res



