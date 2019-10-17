# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.

# It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
 

# Constraints:

# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lower case English letters.

# recursive approach
def removeDuplicates(self, s, k):
    if len(s) < 2: return s
    
    i = 1
    count = 1
    changed = False
    
    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
        else:
            count = 1
        
        if count == k:
            s = s[:i - k + 1] + s[i + 1:]
            changed = True
            i = i - k + 1
        
        i += 1
    
    if not changed:
        return s
    else:
        return self.removeDuplicates(s, k)

# stack based approach
def removeDuplicates(self, s, k):
    if len(s) < 2: return s
    
    stack = []
    for i in s:
        if stack and i == stack[-1][0]:
            stack[-1][1] += 1
            
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([i, 1])
    
    return ''.join([t[0] * t[1] for t in stack])