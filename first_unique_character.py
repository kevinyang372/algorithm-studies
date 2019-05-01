# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

def first_unique_character(s):

    dict_lookup = {}

    for i in s:
        if i in dict_lookup.keys():
            dict_lookup[i] += 1
        else:
            dict_lookup[i] = 0

    for t in dict_lookup.keys():
        if dict_lookup[t] == 0:
            return s.index(t)

    return -1