# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: "bcabc"
# Output: "abc"
# Example 2:

# Input: "cbacdcbc"
# Output: "acdb"

def removeDuplicateLetters(self, s):
        
    c = collections.Counter(s)
    
    def traverse(s, c, remove):
        if not s: return ''
        
        i = 0
        while i < len(s) and s[i] in remove:
            i += 1
            
        if i == len(s):
            return ''
        else:
            smallest = s[i]
            
        ind = i
        temp = dict(c)
        
        while i < len(s) and temp[s[i]] > 1:
            
            if s[i] in remove:
                i += 1
                continue
                
            if s[i] < smallest:
                c = dict(temp)
                smallest = s[i]
                ind = i
                
            temp[s[i]] -= 1
            i += 1
        
        if i < len(s) and smallest > s[i]:
            temp[s[i]] -= 1
            return s[i] + traverse(s[i + 1:], temp, remove)
        else:
            if c[s[ind]] > 1:
                remove.add(s[ind])
            return s[ind] + traverse(s[ind + 1:], c, remove)

    return traverse(s, c, set())