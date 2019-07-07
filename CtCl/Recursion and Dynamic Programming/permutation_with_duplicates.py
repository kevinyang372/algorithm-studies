# Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.

def permutation(s):
    if len(s) < 2: return [s]
    return list(set([t[:i] + s[0] + t[i:] for t in permutation(s[1:]) for i in range(len(t) + 1)]))

# better average case scenario

import collections

def permutation_i(s):
    if len(s) < 2: return [s]
    
    h = collections.Counter(s)
    return helper(h)

def helper(h):
    if len(h.keys()) == 1:
        k = next(iter(h))

        return [str(k) * h[k]]

    res = []
    for m in h.keys():
        if h[m] > 0:
            copy = dict(h)

            if copy[m] == 1:
                copy.pop(m)
            else:
                copy[m] -= 1

            res += [m + t for t in helper(copy)]

    return res 

