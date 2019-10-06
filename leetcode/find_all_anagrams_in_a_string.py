# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
import collections

def findAnagrams(s, p):

    count = 1
    d = collections.Counter()
    total = 0

    for i in p:
        if d[i] > 0:
            total += d[i]
            continue
        d[i] = count
        total += count
        count += 1

    val = [0] * len(s)
    res = []
    
    for key, v in enumerate(s):
        val[key] = d[v]
        if key >= len(p) - 1:
            if sum(val[key-len(p)+1:key+1]) == total:
                res.append(key-len(p)+1)
    
    return res


# sliding window
def findAnagrams(self, s, p):
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res