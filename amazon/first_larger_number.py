# Create list of number and first larger number in array. Only in linear time.
# Eg: input: [2,1,3,9]
# otp: [[2,3],
# [1,3],
# [3,9],
# [9,-1]]

def firstLarger(lis):
    if not lis: return []

    res = []
    stack = []

    for ind, val in enumerate(lis):
        while stack and lis[stack[-1]] < val:
            n = stack.pop()
            res[n][1] = val

        stack.append(ind)
        res.append([val, -1])

    return res