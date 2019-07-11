# Runtime O(logN)
def binarySearch(num, target):

    if not num: return False

    mid = len(num) // 2

    if num[mid] == target:
        return mid
    elif num[mid] < target:
        t = mid + binarySearch(num[mid + 1:], target) + 1
    else:
        t = binarySearch(num[:mid], target)

    return t
