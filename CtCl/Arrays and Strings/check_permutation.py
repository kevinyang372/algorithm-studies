# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(i1, i2):

    if len(i1) != len(i2): return False

    return sorted(i1) == sorted(i2)

# Right answer

import collections

def check_permutation(i1, i2):

    if len(i1) != len(i2): return False

    d = collections.Counter()

    for t in i1:
        d[t] += 1

    for t in i2:
        if d[t] == 0:
            return False
        d[t] -= 1

    return True