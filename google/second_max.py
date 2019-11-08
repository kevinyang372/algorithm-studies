# Given an array of integers, find the second max using only the function compare(a, b) that compares two integers and returns the maximum of the two. The solution must use the function compare(a, b) minimum number of times.

# PS: You can assume that the array doesn't contain any duplicates and all the integers are positive

def compare(a, b):
    return max(a, b)

def secondMax(arr):
    if len(arr) < 2: return -1
    d = {}

    def split(subarr):
        if len(subarr) == 1:
            return subarr[0]
        if len(subarr) == 2:
            res = compare(subarr[0], subarr[1])
            if res == subarr[0]:
                d[subarr[0]] = compare(d.get(subarr[0], -float('inf')), subarr[1])
            else:
                d[subarr[1]] = compare(d.get(subarr[1], -float('inf')), subarr[0])
            return res

        left = split(subarr[:len(subarr) // 2])
        right = split(subarr[len(subarr) // 2:])

        res = compare(left, right)
        if res == left:
            d[left] = compare(d.get(left, -float('inf')), right)
        else:
            d[right] = compare(d.get(right, -float('inf')), left)

        return res

    maxVal = split(arr)
    return d[maxVal]