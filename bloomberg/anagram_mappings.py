# Given 2 strings what is the number of changes to one of them for the strings to become anagrams.
import collections

def mapAnagram(s1, s2):

    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)

    skippable = 0
    for i in c1.keys():
        skippable += min(c1[i], c2[i])

    return max(len(s1), len(s2)) - skippable
