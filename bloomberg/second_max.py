# Second highest number in an array  

def secondHighest(arr):
    if len(arr) < 2: return 

    stack = [-float('inf'), -float('inf')]

    for i in arr:
        if i > stack[1]:
            stack[1], stack[0] = i, stack[1]
        elif i > stack[0]:
            stack[0] = i

    return stack[0]