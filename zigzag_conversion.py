# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

def convert(s, numRows):
        
    if numRows == 1: return s
    
    ind = 0
    d = collections.defaultdict(str)
    count = 0
    direction = 1
    
    while count < len(s):
        d[ind] += s[count]
        
        if ind == numRows - 1:
            direction = -1
            
        ind += direction
        
        if ind == 0:
            direction = 1
        
        count += 1
            
    res = ''
    for i in range(numRows):
        res += d[i]
        
    return res