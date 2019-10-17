# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

def lengthOfLongestSubstringKDistinct(self, s, k):
        
        if not s: return 0
        
        d = collections.Counter()
        i = j = 0
        
        max_length = 0
        
        while j < len(s):
            if len(d) <= k:
                d[s[j]] += 1
                j += 1
            else:
                max_length = max(max_length, j - i - 1)
                
                while len(d) > k:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        d.pop(s[i])
                    i += 1
        
        if len(d) <= k:
            max_length = max(max_length, j - i)
        else:
            max_length = max(max_length, j - i - 1)
        
        return max_length