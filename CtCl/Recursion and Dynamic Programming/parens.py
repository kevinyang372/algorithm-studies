#  Implement an algorithm to print all valid (Le., properly opened and closed) combinations of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output:«())),«()()), «() ()J
# () ( () ) J
# () () (

def parens(num):

    if num == 0: return
    if num == 1: return ['()']

    res = set()
    temp = parens(num - 1)

    for i in temp:
        res.add('()' + i)
        res.add(i + '()')
        res.add('(' + i + ')')

    return list(res)
