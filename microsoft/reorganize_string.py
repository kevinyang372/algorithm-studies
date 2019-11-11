# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# Example 1:

# Input: S = "aab"
# Output: "aba"
# Example 2:

# Input: S = "aaab"
# Output: ""
# Note:

# S will consist of lowercase letters and have length in range [1, 500].

def reorganizeString(self, S):
        
    res = sorted([(S.count(c), c) for c in set(S)])
    A = []
    
    for count, val in res:
        if count > (len(S) + 1) // 2:
            return ""
        A.extend(val * count)
    
    ans = [None] * len(S)
    ans[::2], ans[1::2] = A[len(S) // 2:], A[:len(S) // 2]
    return "".join(ans)