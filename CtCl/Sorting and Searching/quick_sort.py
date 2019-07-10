# Runtime O(NlogN) - average, O(N^2) - worst, Memory O(logN)
def quickSort(num):

    if len(num) < 2: return num

    less = []
    more = []
    equal = [num[0]]

    for i in range(1, len(num)):
        if num[i] < num[0]:
            less.append(num[i])
        elif num[i] == num[0]:
            equal.append(num[i])
        else:
            more.append(num[i])

    return quickSort(less) + equal + quickSort(more)