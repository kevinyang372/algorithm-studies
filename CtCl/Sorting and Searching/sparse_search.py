# Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.
# EXAMPLE
# Input: ball,{"at", "", "", "", "ball", tt" , u", "car", (tJJ, (OJ, "dad", ""U"}


# Output: 4

def sparseSearch(lis, target):

    if not lis: return

    origin = mid = len(lis) // 2

    while not lis[mid]:
        mid += 1

    if lis[mid] == target:
        return mid
    elif lis[mid] > target:
        return sparseSearch(lis[:origin], target)
    else:
        return mid + sparseSearch(lis[mid + 1:], target) + 1

    return False
