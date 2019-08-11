# You are given a string a_{cat,dog}_is_with_{sarah,mike}
# Return the outputs as:
# a_cat_is_with_sarah
# a_cat_is_with_mike
# a_dog_is_with_sarah
# a_dog_is_with_mike

def braceExpansion(s):

    if '{' not in s: return [s]

    i = s.index('{')
    t = s.index('}')

    choices = s[i + 1: t].split(',')
    res, temp = [], braceExpansion(s[t + 1:])

    for n in choices:
        for m in temp:
            res.append(s[:i] + n + m)

    return res