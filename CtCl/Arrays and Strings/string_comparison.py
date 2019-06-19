# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

import collections

def string_comparison(s):

    if len(s) < 2: return s

    d = collections.Counter()

    for i in s:
        d[i] += 1

    fin = ""
    for k, v in d.items():
        fin += "%s%s" % (k, v)

    return min(fin, s, key=len)

