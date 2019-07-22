# Write an algorithm to help James find the sets of foreground and background application pairs that optimally utilize the given device for a given list of foreground and background applications

# Input:
# deviceCapacity: an integer representing the maximum capacity of the given device
# foregroundAppList: a list of pairs of integers where the first integer represents the unique ID of a foreground application and the second integer represents the amount of memory required

# Example:
# Input:
# deviceCapacity = 10
# foregroundAppList = [[1,3], [2,5], [3,7], [4,10]]
# backgroundAppList = [[1,2], [2,3], [3,4], [4,5]]

# O(N^2)
def optimalPair(cap, foreground, background):

    f = {i:v for (i, v) in foreground}
    b = {i:v for (i, v) in background}

    max_val = 0
    max_lis = []

    for i in f.keys():
        for t in b.keys():
            if f[i] + b[t] > max_val and f[i] + b[t] <= cap:
                max_val = f[i] + b[t]
                max_lis = [[i, t]]
            elif f[i] + b[t] == max_val:
                max_lis.append([i, t])

    return max_lis