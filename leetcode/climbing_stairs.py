# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# Bruteforce
def climbStairs(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2

    return climbStairs(n - 1) + climbStairs(n - 2)

# Dynamic Programming
def climbStairs_dp(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2

    steps = [None for i in range(n)]

    steps[0] = 1
    steps[1] = 2

    for i in range(2, n):
        steps[i] = steps[i - 1] + steps[i - 2]

    return steps[n - 1]