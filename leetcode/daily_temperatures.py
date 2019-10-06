# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

def dailyTemperatures(T):

    if not T: return []

    output = [0] * len(T)
    staging = []

    for t in range(len(T) - 1):

        if T[t] < T[t + 1]:
            output[t] = 1
        else:
            staging.append([t, T[t]])

        k = 0
        while k < len(staging):
            if staging[k][1] < T[t + 1]:
                output[staging[k][0]] = t - staging[k][0] + 1
                staging.pop(k)
                k -= 1
            k += 1

    return output

# improved stack solution

def dailyTemperatures(T):

    output = [0] * len(T)
    stack = []

    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            output[cur] = i - cur
        stack.append(i)

    return output