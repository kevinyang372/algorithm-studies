# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

# Example 1:

# Input:
# s = "aaabb", k = 3

# Output:
# 3

# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input:
# s = "ababbc", k = 2

# Output:
# 5

# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# hashmap TLE
def longestSubstring(self, s, k):
        
    if len(s) < k: return 0
    
    d = collections.defaultdict(collections.Counter)
    d[-1] = collections.Counter()
    max_length = 0
    
    for i in range(len(s)):
        d[i] = collections.Counter(d[i - 1])
        d[i][s[i]] += 1

        if i >= k - 1:
            for t in range(-1, i - max_length):
                passed = True
                for ind, v in (d[i] - d[t]).items():
                    if v < k:
                        passed = False
                        break
                if passed: 
                    max_length = i - t
                    break
    
    return max_length

# dp solution by splitting the string by least frequent elements
def longestSubstring(self, s, k):
    if len(s) < k: return 0

    for i in set(s):
        if s.count(i) < k:
            return max(self.longestSubstring(t, k) for t in s.split(i))

    return len(s)