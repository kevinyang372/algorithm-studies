# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

# Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

# Example 1:

# Input: "banana"
# Output: "ana"
# Example 2:

# Input: "abcd"
# Output: ""
 

# Note:

# 2 <= S.length <= 10^5
# S consists of lowercase English letters.

def longestDupSubstring(self, S: str) -> str:
        
    mod = 2**63 - 1
    
    def checkDupWithLengthK(k):
        visited = set()
        p = pow(26, k, mod)
        
        start = 0
        for i in range(k):
            start = (start * 26 + ord(S[i]) - 96) % mod
        
        visited.add(start)
        
        for t in range(len(S) - k):
            start = (start * 26 + ord(S[t + k]) - 96 - (ord(S[t]) - 96) * p) % mod
            if start in visited: return S[t + 1:t + k + 1]
            visited.add(start)
        
        return ''
    
    low, high = 0, len(S)
    res = ''
    
    while low < high:
        mid = (low + high) // 2
        temp = checkDupWithLengthK(mid)
        if len(temp) > len(res):
            res = temp
            low = mid + 1
        else:
            high = mid
            
    return res