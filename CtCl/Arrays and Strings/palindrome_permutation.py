# Given a string, write a function to check if it is a permutation of a palin- drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

import collections

def palindrome_permutation(inp):

    if len(inp) < 2: return True

    inp = inp.lower().replace(" ", "")
    d = collections.Counter()

    for i in inp:
        d[i] += 1

    if len(inp) % 2 == 0:
        allow_one = False
    else:
        allow_one = True

    for k, v in d.items():
        if v % 2 == 1:
            if not allow_one:
                return False
            allow_one = False

    return True