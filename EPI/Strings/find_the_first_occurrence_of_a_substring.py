# Given two strings s (the "search string") and t (the "text"), find the first occurrence of s in t

# pattern matching with kmp
def kmp(pattern, s):
    dp = [0] * len(pattern)
    
    for i, v in enumerate(pattern):
        if i > 0 and v == pattern[dp[i - 1]]:
            dp[i] = dp[i - 1] + 1
        
    i = j = 0
    while i < len(s):
        if s[i] == pattern[j]:
            i += 1
            j += 1
            
            if j == len(pattern):
                return i - j
        elif j > 0:
            j = dp[j - 1]
        else:
            i += 1
            
    return -1