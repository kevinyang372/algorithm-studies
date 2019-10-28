# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]

# Output: 
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]

# Output: 
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

def findLongestWord(self, s, d):

    res = ""
    for sub in d:
        if len(sub) >= len(res):
            included = True
            i = j = 0
            
            while i < len(s) and j < len(sub):
                if s[i] != sub[j]:
                    i += 1
                else:
                    i += 1
                    j += 1
            
            if j < len(sub):
                continue
            elif len(sub) > len(res) or (len(sub) == len(res) and sub < res):
                res = sub

    return res