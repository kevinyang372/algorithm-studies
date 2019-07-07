# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.

def coins(n, lib):

    if n == 0: return [[]]
    if n < min(lib): return []

    res = []
    for i in lib:
        temp = coins(round(n - i, 3), lib)
        if temp:
            for t in temp:
                t.append(i)
                res.append(t)

    return res