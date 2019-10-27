# Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

# If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

# Example 1:

# Input: 
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must occur in order.
 

# Note:

# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].

# O(N^2) TLE
def minWindow(self, S, T):
    i = 0
    min_l = ""
    while i < len(S) - len(T) + 1:
        if S[i] == T[0]:
            t1, t2 = i + 1, 1
            while t1 < len(S) and t2 < len(T):
                if S[t1] == T[t2]:
                    t1 += 1
                    t2 += 1
                else:
                    t1 += 1
            
            if t2 == len(T):
                temp = S[i:t1]
                if min_l == "" or len(min_l) > len(temp):
                    min_l = temp
        
        i += 1
    
    return min_l

# O(N) dp
def minWindow(self, S, T):
    n = len(S)
    m = len(T)
    
    dic = dict()
    for i, s in enumerate(T):
        dic.setdefault(s, []).append(i)
        
    dp = [-1 for i in xrange(m)]
    
    count = n+1
    start = -1
    
    for index, c in enumerate(S):
        if c in dic:
            for i in dic[c][::-1]:
                if i == 0:
                    dp[i] = index
                else:
                    dp[i] = dp[i-1]
                if i == m-1 and dp[i] >= 0 and index - dp[i]+1 < count:
                    count = index - dp[i] + 1
                    start = dp[i]
    if dp[-1] < 0:
        return ""
    return S[start:start+count]