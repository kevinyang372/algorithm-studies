# Giving a tuple (ord, str) of type (string, string), check whether all the characters that appear in both str and ord are in the order of ord.
# Examples:
# (abc, qaqbqc) -> True
# (abc, aaaqbbb) -> True
# (abc, caaabbbccc) -> False

def checkOrder(base, arr):

    d = {}
    count = 0
    for i in base:
        d[i] = count
        count += 1

    cur = 0
    for m in arr:
        if m in d:
            if d[m] < cur:
                return False
            cur = d[m]

    return True