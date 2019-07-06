# Write a method to compute all permutations of a string of unique chara c t ers .

def permutation(s):
    if len(s) < 2: return [s]
    return [t[:i] + s[0] + t[i:] for t in permutation(s[1:]) for i in range(len(t) + 1)]