# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

def tripleStep(n):

    mat = [0] * (n + 1)
    mat[0] = 1

    for i in range(1, len(mat)):
        mat[i] = sum([mat[i - k] for k in range(1, 4) if i - k >= 0])

    return mat[-1]