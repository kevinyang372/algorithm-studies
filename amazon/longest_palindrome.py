# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

def longestPalindrome(self, s):
    s = collections.Counter(s)
    
    max_odd = 0
    count = 0
    
    for i in s:
        if s[i] % 2 == 0:
            count += s[i]
        else:
            count += s[i] - 1
            max_odd = 1
    
    return count + max_odd