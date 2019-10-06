# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
# Example 5:

# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

def isMatch(s, p):

    ind = 0

    for i in range(len(s)):

        cur = s[i]
        
        if ind >= len(p):
            return False
        
        while ind < len(p):

            if ind + 1 < len(p) and p[ind + 1] == '*':
                pre = p[ind]
                temp = 0
                while i + temp < len(s) and s[i + temp] == pre:
                    temp += 1
                if temp > 0:
                    i += temp
                    break
                else:
                    ind += 2
            elif p[ind] == s[i] or p[ind] == '.':
                ind += 1
                break
            else:
                return False

    return True

cache = {}
def isMatch(self, s, p):
    if (s, p) in self.cache:
        return self.cache[(s, p)]
    if not p:
        return not s
    if p[-1] == '*':
        if self.isMatch(s, p[:-2]):
            self.cache[(s, p)] = True
            return True
        if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
            self.cache[(s, p)] = True
            return True
    if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
        self.cache[(s, p)] = True
        return True
    self.cache[(s, p)] = False
    return False
