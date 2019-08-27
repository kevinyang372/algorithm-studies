# Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3
# Note:

# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].

def findLUSlength(self, strs):
    strs.sort(key=lambda x: len(x), reverse=True)
    
    if len(strs[0]) == 1:
        strs.sort()
    
    seen = set()
    i = 0
    
    def subseq(s, l, s1, l1):
        if s1 == 0: return True
        if l1 == 0: return False
        
        if s[s1 - 1] == l[l1 - 1]:
            return subseq(s, l, s1 - 1, l1 - 1)
        else:
            return subseq(s, l, s1, l1 - 1)
        
    
    while i < len(strs):
        if (i < len(strs) - 1 and strs[i] == strs[i + 1]) or strs[i] in seen:
            seen.add(strs[i])
            i += 1
            continue
        
        uniq = True
        for t in seen:
            if subseq(strs[i], t, len(strs[i]), len(t)):
                uniq = False
                break
        
        seen.add(strs[i])
        if uniq:
            return len(strs[i])
        
        i += 1
    
    return -1