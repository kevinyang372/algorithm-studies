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
    for key, v in enumerate(s):
        val[key] = d[v]

    res = []
    for i in range(len(val)):
        if sum(val[i:i + len(p)]) == total:
            res.append(i)

    return res