# Given a sorted ascending array, return a array which has it's elements in such a manner that:
# even index element >= all previous elements
# odd index element <= all previous elements

# E.g. [1, 2, 3, 4, 6] -> [3, 2, 4, 1, 6] and [0, 1, 2, 3] -> [2, 1, 3, 0]

def evenOdd(arr):
    arr[::2], arr[1::2] = arr[:len(arr) // 2], arr[len(arr) // 2:][::-1]
    return arr