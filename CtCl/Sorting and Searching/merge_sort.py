# Runtime O(NlogN), Space: depends
def mergeSort(num):

    if len(num) < 2: return num
    if len(num) == 2: return [num[0], num[1]] if num[0] < num[1] else [num[1], num[0]]

    arr1 = mergeSort(num[:len(num) // 2])
    arr2 = mergeSort(num[len(num) // 2:])

    res = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))

    res += arr1 + arr2

    return res