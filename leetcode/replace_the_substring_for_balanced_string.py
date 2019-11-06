# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

# A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

# Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

# Return 0 if the string is already balanced.

 

# Example 1:

# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.
# Example 2:

# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
# Example 3:

# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER". 
# Example 4:

# Input: s = "QQQQ"
# Output: 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
 

# Constraints:

# 1 <= s.length <= 10^5
# s.length is a multiple of 4
# s contains only 'Q', 'W', 'E' and 'R'.

def balancedString(self, s):
        
    c = collections.Counter(s)
    l = len(s) // 4
    
    window = {}
    for key in c:
        if c[key] > l:
            window[key] = c[key] - l
            
    if not window: return 0
    
    i, j = 0, 1
    temp = collections.Counter([s[0]])
    min_length = float('inf')
    
    while j < len(s) + 1:
        flag = True
        for sub in window:
            if temp[sub] < window[sub]:
                flag = False
                break
                
        if flag and i < j:
            min_length = min(min_length, j - i)
            temp[s[i]] -= 1
            i += 1
        elif j < len(s):
            temp[s[j]] += 1
            j += 1
        else:
            break
    
    return min_length