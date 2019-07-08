# Michelle has created a word game for her students. The word game begins with Michelle writing a string and a number, K, on the board. The students have to ﬁnd the substrings of size K with K distinct characters.

# Write an algorithm to help the students ﬁnd the correct answer. If the given string does not have K distinct characters then output an empty list.
# Input
# The input to the function/method consists of two arguments -
# inputStr, representing the string written by the teacher;
# num , an integer representing the number, K, written by the teacher on the board.

# Output
# Return distinct substrings of input string of size K with K distinct characters.

# Constraints
# 0 ≤  num  ≤ 26

# Note

# The input string consists of only lowercase letters of the English alphabet. Substrings are not necessarily distinct.

# Examples
# Input:
# inputStr = awaglknagawunagwkwagl
# num = 4

# Output:
# {wagl, aglk, glkn, lkna, knag, gawu, awun, wuna, unag, nagw, agwk, kwag}

# Explanation:
# Substrings in order are: wagl, aglk, glkn, lkna, knag, gawu, awun, wuna, unag, nagw, agwk, kwag, wagl
# "wagl" is repeated twice, but is included in the output once

def wordGame(s, k):

    res = set()
    for i in range(len(s) - k):
        if len(set(s[i:i + k])) == len(s[i:i + k]):
            res.add(s[i:i + k])

    return list(res)