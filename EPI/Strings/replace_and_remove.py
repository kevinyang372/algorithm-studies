# Consider the following two rules that are applied to an arryay of characters
# - Replace each 'a' by two 'd's
# - Delete each entry containing a 'b'
# e.g. <'a', 'c', 'd', 'b', 'b', 'c', 'a'> -> <'d', 'd', 'c', 'd', 'c', 'd', 'd'>

def update(arr):

    curr = count = 0
    for i in range(len(arr)):
        if arr[i] != 'b':
            arr[curr] = arr[i]
            curr += 1
        if arr[i] == 'a':
            count += 1


    curr -= 1
    i = len(arr) - 1

    while i > -1:
        if arr[curr] != 'a':
            arr[i] = arr[curr]
            curr -= 1
            i -= 1
        else:
            arr[i] = 'd'
            arr[i - 1] = 'd'
            i -= 2
            curr -= 1

    return arr