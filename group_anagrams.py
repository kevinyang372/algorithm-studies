# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

import collections

def groupAnagrams(strs):

    if not strs: return

    res = []
    counters = []

    for e in strs:
        d = collections.Counter()
        for m in e:
            d[m] += 1

        if d in counters:
            res[counters.index(d)].append(e)
        else:
            counters.append(d)
            res.append([e])

    return res

# Hash Maps
def groupAnagrams(strs):

    d = collections.Counter([tuple(sorted(s)) for s in strs])
    return filter(lambda x: count([tuple(sorted(x))]) > 1, strs)