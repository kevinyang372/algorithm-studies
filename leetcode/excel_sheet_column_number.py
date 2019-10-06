# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28
# Example 3:

# Input: "ZY"
# Output: 701

def titleToNumber(s):
    return sum([(ord(v) - 64) * 26 ** (len(s) - i - 1) for i, v in enumerate(s)])