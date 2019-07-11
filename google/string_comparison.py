# One string is strictly smaller than another when the frequency of occurrence of the smallest character in the string is less than the frequency of occurrence of the smallest character in the comparison string.

# For example, string "abcd" is smaller than string "aaa" because the smallest character in "abcd" is 'a', with a frequency of 1. The smallest character in "aaa" is also 'a', but with a frequency of 3. In another example, string "a" is smaller than string "bb" because the smallest character in "a" is 'a' with a frequency of 1, and the smallest character in "bb" is 'b' with a frequency of 2.

# Write a function that, given string A and string B, returns an array C of integers. The number of strings in A which are strictly smaller than the comparison string in B.

# Given strings A and B such that:
# A = "abcd aabc bd"
# B = "aaa aa"

# the function should return [3, 2].

import collections

def stringComparison(s1, s2):

    s1 = [collections.Counter(i)[sorted(i)[0]] for i in s1.split(' ')]
    s2 = [collections.Counter(i)[sorted(i)[0]] for i in s2.split(' ')]

    return [sum([1 for n in s1 if m > n]) for m in s2]