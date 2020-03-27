# You are given a string s containing lowercase letters and an integer k. You need to :

# First, change some characters of s to other lowercase English letters.
# Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
# Return the minimal number of characters that you need to change to divide the string.

 

# Example 1:

# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
# Example 2:

# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
# Example 3:

# Input: s = "leetcode", k = 8
# Output: 0
 

# Constraints:

# 1 <= k <= s.length <= 100.
# s only contains lowercase English letters.

def palindromePartition(self, s: str, k: int) -> int:
        
    d = {}
    def minToPalindrome(m, j):
        if (m, j) in d: return d[m, j]
        mm, jj = m, j
        c = 0
        while mm < jj:
            if s[mm] != s[jj]:
                c += 1
            mm += 1
            jj -= 1
        d[m, j] = c
        return c
    
    sd = {}
    def cut(i, k):
        if (i, k) in sd: return sd[i, k]
        if len(s) - i == k: return 0
        if len(s) - i < k: return float('inf')
        if k == 1: return minToPalindrome(i, len(s) - 1)
        
        min_val = float('inf')
        for di in range(i, len(s) - k + 1):
            min_val = min(min_val, minToPalindrome(i, di) + cut(di + 1, k - 1))
            
        sd[i, k] = min_val
        return min_val
    
    return cut(0, k) 